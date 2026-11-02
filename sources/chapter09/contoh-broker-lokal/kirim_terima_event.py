# Contoh kirim dan terima event JanjiTemuDibuat lewat RabbitMQ lokal (Bab 09).
# Pakai: docker compose up -d, pip install pika, lalu jalankan
#   python kirim_terima_event.py kirim    (mengirim event yang sama dua kali)
#   python kirim_terima_event.py terima   (memproses event, duplikat dilewati)
"""Meniru pengiriman at-least-once dan penerima yang idempoten.

Pengirim sengaja menerbitkan event yang sama dua kali, seperti pengirim yang
mengulang karena konfirmasi dari broker tidak sampai. Penerima mencatat id
event yang sudah diproses di SQLite, sehingga kiriman kedua dikenali sebagai
duplikat dan pengingat tidak terkirim dua kali.
"""

import argparse
import json
import sqlite3
import uuid
from datetime import datetime, timezone

import pika

# Alamat broker sesuai docker-compose.yml; 5672 adalah port bawaan AMQP.
ALAMAT_BROKER = "localhost"
PORT_BROKER = 5672

# Exchange bertipe topic: banyak layanan dapat berlangganan event yang sama
# tanpa pengirim perlu mengetahui siapa saja pelanggannya.
NAMA_EXCHANGE = "medikara.janji-temu"
KUNCI_RUTE = "janji-temu.dibuat"

# Antrean milik layanan notifikasi. Layanan lain membuat antreannya sendiri,
# sehingga gangguan pada satu pelanggan tidak menahan pelanggan lain.
NAMA_ANTREAN = "notifikasi.janji-temu-dibuat"

# Jumlah kiriman event yang sama untuk meniru pengiriman ulang.
JUMLAH_KIRIMAN = 2

# Mode 2 membuat pesan ditulis ke disk sehingga bertahan saat broker restart.
MODE_PESAN_PERSISTEN = 2

# Berkas SQLite berisi id event yang sudah diproses penerima.
BERKAS_EVENT_TERPROSES = "event_terproses.db"


def buka_kanal():
  """Membuka koneksi ke broker lalu memastikan exchange dan antrean tersedia.

  Deklarasi di RabbitMQ aman diulang, sehingga pengirim maupun penerima boleh
  dijalankan lebih dahulu tanpa saling menunggu.
  """
  koneksi = pika.BlockingConnection(
    pika.ConnectionParameters(host=ALAMAT_BROKER, port=PORT_BROKER)
  )
  kanal = koneksi.channel()
  kanal.exchange_declare(
    exchange=NAMA_EXCHANGE, exchange_type="topic", durable=True
  )
  kanal.queue_declare(queue=NAMA_ANTREAN, durable=True)
  kanal.queue_bind(
    queue=NAMA_ANTREAN, exchange=NAMA_EXCHANGE, routing_key=KUNCI_RUTE
  )
  return koneksi, kanal


def susun_event_janji_temu():
  """Menyusun event JanjiTemuDibuat dalam amplop CloudEvents 1.0.

  Atribut id menjadi kunci idempotensi, jadi nilainya harus sama pada setiap
  kiriman ulang. Data pasien hanya berupa nomor rujukan rekaan agar event
  tidak menyebarkan data pribadi ke semua pelanggan.
  """
  return {
    "specversion": "1.0",
    "id": str(uuid.uuid4()),
    "source": "/medikara-plus/janji-temu",
    "type": "example.medikara.janjitemu.dibuat.v1",
    "time": datetime.now(timezone.utc).isoformat(),
    "datacontenttype": "application/json",
    "data": {
      "nomorJanjiTemu": "JT-2026-104233",
      "rujukanPasien": "PSN-7F3A",
      "fasilitas": "RS Medikara Bekasi",
      "poliklinik": "Penyakit Dalam",
      "waktuKunjungan": "2026-11-03T09:30:00+07:00",
    },
  }


def kirim_event():
  """Menerbitkan event yang sama sebanyak JUMLAH_KIRIMAN kali.

  Isi pesan dibuat sekali, sehingga setiap kiriman membawa id yang sama,
  persis seperti pengiriman ulang pada jaminan at-least-once.
  """
  koneksi, kanal = buka_kanal()
  event = susun_event_janji_temu()
  properti = pika.BasicProperties(
    content_type="application/cloudevents+json",
    delivery_mode=MODE_PESAN_PERSISTEN,
  )
  for urutan in range(JUMLAH_KIRIMAN):
    kanal.basic_publish(
      exchange=NAMA_EXCHANGE,
      routing_key=KUNCI_RUTE,
      body=json.dumps(event),
      properties=properti,
    )
    print(f"Kiriman ke-{urutan + 1}: event {event['id']}")
  koneksi.close()


def buka_catatan_terproses():
  """Membuka tabel id event; kunci primer menolak id yang sama dua kali."""
  catatan = sqlite3.connect(BERKAS_EVENT_TERPROSES)
  catatan.execute(
    "CREATE TABLE IF NOT EXISTS event_terproses (id TEXT PRIMARY KEY)"
  )
  return catatan


def tandai_terproses(catatan, id_event):
  """Mencatat id event; False berarti id itu sudah pernah dicatat.

  Pemeriksaan dan pencatatan terjadi dalam satu perintah INSERT,
  sehingga dua penerima yang berjalan bersamaan tidak sama-sama
  lolos.
  """
  try:
    with catatan:
      catatan.execute(
        "INSERT INTO event_terproses (id) VALUES (?)", (id_event,)
      )
    return True
  except sqlite3.IntegrityError:
    return False


def terima_event():
  """Mengambil semua pesan dan memproses setiap event sekali saja.

  Pesan duplikat tetap diakui (ack) agar broker tidak mengirimnya
  terus. Pada sistem nyata, pencatatan id dan efek bisnisnya
  disimpan dalam satu transaksi; contoh ini menyederhanakannya.
  """
  koneksi, kanal = buka_kanal()
  catatan = buka_catatan_terproses()
  while True:
    metode, _properti, isi = kanal.basic_get(queue=NAMA_ANTREAN)
    if metode is None:
      break
    event = json.loads(isi)
    if tandai_terproses(catatan, event["id"]):
      nomor = event["data"]["nomorJanjiTemu"]
      print(f"Proses: pengingat untuk {nomor} dikirim")
    else:
      print(f"Lewati: event {event['id']} sudah pernah diproses")
    kanal.basic_ack(delivery_tag=metode.delivery_tag)
  catatan.close()
  koneksi.close()


def main():
  """Membaca mode dari baris perintah lalu menjalankan pengirim atau penerima."""
  pengurai = argparse.ArgumentParser(description=__doc__)
  pengurai.add_argument("mode", choices=["kirim", "terima"])
  argumen = pengurai.parse_args()
  if argumen.mode == "kirim":
    kirim_event()
  else:
    terima_event()


if __name__ == "__main__":
  main()
