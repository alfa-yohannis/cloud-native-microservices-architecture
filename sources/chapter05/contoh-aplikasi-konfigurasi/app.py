# Contoh aplikasi Bab 05: konfigurasi dari environment variable dan log ke stdout.
# Pakai: isi variabel seperti di contoh-bogor.env, lalu jalankan python app.py.
"""Aplikasi contoh jadwal dokter yang mengikuti faktor III, VI, VII, IX, dan XI.

Konfigurasi dibaca dari environment variable agar satu kode yang sama dapat
dipasang di lima rumah sakit tanpa diubah. Log ditulis ke stdout sebagai satu
baris JSON per kejadian, sehingga platform yang mengumpulkan dan menyimpannya.
Aplikasi tidak menyimpan state di memori, sehingga proses tambahan dapat
dijalankan kapan saja untuk menambah kapasitas.
"""

import json
import os
import signal
import sys
import time
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer

# Variabel yang wajib ada. Aplikasi menolak menyala bila salah satunya kosong,
# karena konfigurasi yang hilang lebih baik ketahuan saat mulai.
VARIABEL_WAJIB = ("KODE_RUMAH_SAKIT", "ALAMAT_BASIS_DATA", "KUNCI_AKSES_BPJS")

# Port bawaan bila PORT tidak diisi; platform biasanya mengisinya sendiri.
PORT_BAWAAN = 8080

# Alamat dengar untuk semua antarmuka jaringan, agar platform dapat meneruskan
# permintaan ke proses ini dari luar container.
ALAMAT_DENGAR = "0.0.0.0"

# Kode keluar untuk kegagalan konfigurasi dan untuk berhenti normal. Platform
# membaca kode ini untuk membedakan proses yang gagal dari proses yang selesai.
KODE_KELUAR_GAGAL = 1
KODE_KELUAR_NORMAL = 0

# Jumlah angka di belakang koma untuk lama waktu mulai yang dicatat ke log.
PRESISI_DETIK = 3


def tulis_log(tingkat, kejadian, **rincian):
  """Menulis satu kejadian sebagai satu baris JSON ke stdout.

  Mengapa: aplikasi tidak mengurus berkas log, rotasi, atau penyimpanan.
  Akibat: platform dapat mengumpulkan log semua proses ke satu tempat,
  sehingga satu pertanyaan audit dijawab dengan satu pencarian.
  """
  catatan = {
      "waktu": datetime.now(timezone.utc).isoformat(),
      "tingkat": tingkat,
      "kejadian": kejadian,
  }
  catatan.update(rincian)
  print(json.dumps(catatan), flush=True)


def baca_konfigurasi(lingkungan):
  """Mengambil konfigurasi dari environment variable.

  Mengapa: nilai yang berbeda antarlokasi tidak boleh tertanam di kode.
  Akibat: bila ada variabel wajib yang kosong, aplikasi berhenti dengan
  pesan yang jelas, bukan gagal diam-diam saat melayani pasien.
  """
  kosong = [nama for nama in VARIABEL_WAJIB if not lingkungan.get(nama)]
  if kosong:
    tulis_log("error", "konfigurasi_tidak_lengkap", variabel=kosong)
    sys.exit(KODE_KELUAR_GAGAL)
  return {
      "kode_rumah_sakit": lingkungan["KODE_RUMAH_SAKIT"],
      "alamat_basis_data": lingkungan["ALAMAT_BASIS_DATA"],
      "kunci_akses_bpjs": lingkungan["KUNCI_AKSES_BPJS"],
      "port": int(lingkungan.get("PORT", PORT_BAWAAN)),
  }


class PenanganJadwal(BaseHTTPRequestHandler):
  """Melayani permintaan jadwal tanpa menyimpan state di memori proses.

  Mengapa: setiap permintaan berdiri sendiri, sehingga proses mana pun dapat
  melayaninya. Akibat: kapasitas ditambah cukup dengan menjalankan proses
  tambahan di belakang penyeimbang beban.
  """

  def do_GET(self):
    """Menjawab permintaan jadwal dan mencatatnya ke log tanpa data rahasia."""
    konfigurasi = self.server.konfigurasi
    isi = json.dumps({
        "rumah_sakit": konfigurasi["kode_rumah_sakit"],
        "jadwal": [],
    }).encode("utf-8")
    self.send_response(HTTPStatus.OK)
    self.send_header("Content-Type", "application/json")
    self.end_headers()
    self.wfile.write(isi)
    tulis_log("info", "jadwal_diminta", alamat=self.path,
              rumah_sakit=konfigurasi["kode_rumah_sakit"])

  def log_message(self, pola, *argumen):
    """Mematikan log bawaan agar semua log memakai format JSON yang sama."""
    return


def berhenti_dengan_rapi(nomor_sinyal, bingkai):
  """Menangani SIGTERM yang dikirim platform.

  Mengapa: platform mematikan proses saat kapasitas dikurangi atau saat versi
  baru dipasang. Akibat: proses mencatat alasan berhenti lalu keluar bersih
  dalam hitungan detik.
  """
  tulis_log("info", "proses_berhenti", sinyal=nomor_sinyal)
  sys.exit(KODE_KELUAR_NORMAL)


def jalankan():
  """Menyalakan server dan mencatat lama waktu mulai.

  Mengapa: waktu mulai yang singkat (faktor IX) membuat proses baru berguna
  saat lonjakan. Akibat: angka lama_mulai_detik di log dapat dipantau.
  """
  waktu_mulai = time.monotonic()
  konfigurasi = baca_konfigurasi(os.environ)
  signal.signal(signal.SIGTERM, berhenti_dengan_rapi)
  server = HTTPServer((ALAMAT_DENGAR, konfigurasi["port"]), PenanganJadwal)
  server.konfigurasi = konfigurasi
  lama_mulai = round(time.monotonic() - waktu_mulai, PRESISI_DETIK)
  tulis_log("info", "proses_siap", port=konfigurasi["port"],
            rumah_sakit=konfigurasi["kode_rumah_sakit"],
            lama_mulai_detik=lama_mulai)
  server.serve_forever()


if __name__ == "__main__":
  jalankan()
