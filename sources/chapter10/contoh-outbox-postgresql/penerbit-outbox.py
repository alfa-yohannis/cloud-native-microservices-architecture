# Penerbit outbox Bab 10. Jalankan: python penerbit-outbox.py (butuh psycopg 3).
"""Membaca baris outbox yang belum terbit, menerbitkannya, lalu menandainya.

Broker sungguhan (misalnya RabbitMQ atau Apache Kafka) sengaja diganti dengan berkas
JSON Lines agar contoh dapat dijalankan tanpa memasang broker. Pola pembacaan dan
penandaan tetap sama dengan sistem produksi; hanya tujuan pengirimannya yang berbeda.

Persiapan:
  pip install "psycopg[binary]"
  psql -d medikara -f skema-outbox.sql

Peringatan: jalankan hanya pada basis data PostgreSQL milik sendiri.
"""

import json
import os
import time

import psycopg

# Alamat basis data dibaca dari variabel lingkungan agar kata sandi tidak tertulis
# di kode. Nilai bawaan hanya cocok untuk PostgreSQL lokal milik sendiri.
ALAMAT_BASIS_DATA = os.environ.get(
  "ALAMAT_BASIS_DATA", "postgresql://postgres:postgres@localhost:5432/medikara"
)
# Berkas pengganti broker. Setiap baris berisi satu event dalam format JSON.
BERKAS_BROKER = "event-terbit.jsonl"
# Jumlah baris per putaran dibatasi agar satu transaksi tidak mengunci terlalu lama.
UKURAN_KELOMPOK = 50
# Jeda bila outbox kosong. Makin pendek, makin segar event, makin sering query.
JEDA_DETIK = 2.0

# SKIP LOCKED membuat dua penerbit yang berjalan bersamaan tidak mengambil baris
# yang sama, sehingga penerbit dapat ditambah tanpa saling menunggu.
PERINTAH_AMBIL = """
  SELECT id_event, jenis_event, id_agregat, isi, id
  FROM outbox
  WHERE waktu_terbit IS NULL
  ORDER BY id
  LIMIT %s
  FOR UPDATE SKIP LOCKED
"""
PERINTAH_TANDAI = "UPDATE outbox SET waktu_terbit = now() WHERE id = %s"


def terbitkan(event):
  """Menulis satu event ke berkas pengganti broker.

  Fungsi ini dipisah agar mudah diganti dengan klien broker sungguhan tanpa
  mengubah logika pembacaan outbox.
  """
  with open(BERKAS_BROKER, "a", encoding="utf-8") as berkas:
    berkas.write(json.dumps(event, ensure_ascii=False) + "\n")


def proses_satu_kelompok(koneksi):
  """Menerbitkan satu kelompok baris outbox, lalu mengembalikan jumlahnya.

  Penandaan baru tersimpan setelah penerbitan. Bila proses mati di antara
  keduanya, event yang sama terbit ulang pada putaran berikutnya. Karena itu
  consumer wajib idempoten: jaminannya at-least-once, bukan exactly-once.
  """
  with koneksi.transaction():
    hasil = koneksi.execute(PERINTAH_AMBIL, (UKURAN_KELOMPOK,))
    baris_outbox = hasil.fetchall()
    for id_event, jenis, id_agregat, isi, nomor_baris in baris_outbox:
      terbitkan({"id_event": str(id_event), "jenis": jenis,
                 "id_agregat": id_agregat, "isi": isi})
      koneksi.execute(PERINTAH_TANDAI, (nomor_baris,))
  return len(baris_outbox)


def jalankan_terus():
  """Mengulang pemrosesan sampai dihentikan dengan Ctrl+C.

  Koneksi memakai autocommit agar setiap blok transaction() menjadi satu
  transaksi yang jelas batasnya, bukan transaksi panjang yang tidak pernah
  ditutup.
  """
  with psycopg.connect(ALAMAT_BASIS_DATA, autocommit=True) as koneksi:
    while True:
      jumlah = proses_satu_kelompok(koneksi)
      if jumlah:
        print(f"{jumlah} event terbit ke {BERKAS_BROKER}")
      else:
        time.sleep(JEDA_DETIK)


if __name__ == "__main__":
  try:
    jalankan_terus()
  except KeyboardInterrupt:
    print("Penerbit dihentikan.")
