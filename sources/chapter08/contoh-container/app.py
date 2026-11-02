# Layanan jadwal dokter tiruan untuk pendalaman Bab 08. Jalankan dengan
# python app.py, lalu buka http://localhost:8080/jadwal di peramban.
"""Layanan jadwal dokter yang sengaja dibuat kecil.

Layanan hanya memakai pustaka standar Python. Akibatnya image tidak membawa
dependensi pihak ketiga yang versinya bisa berbeda antarlingkungan, sehingga
masalah "jalan di Jakarta, gagal di Bandung" tidak muncul dari sisi pustaka.
Seluruh data di berkas ini rekaan dan tidak memuat data pasien.
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# Port dibaca dari variabel lingkungan (faktor konfigurasi pada Bab 5).
# Akibatnya image yang sama berjalan di lingkungan mana pun tanpa dibangun
# ulang.
PORT_BAWAAN = 8080
PORT = int(os.environ.get("PORT", PORT_BAWAAN))

# Nama fasilitas juga konfigurasi, bukan kode: satu image untuk lima rumah
# sakit.
NAMA_FASILITAS = os.environ.get("NAMA_FASILITAS", "RS Medikara Jakarta")

# Alamat semua antarmuka jaringan. Tanpa ini layanan hanya terjangkau dari
# dalam container, dan pemeriksaan kesehatan Kubernetes akan gagal.
ALAMAT_SEMUA_ANTARMUKA = "0.0.0.0"

KODE_BERHASIL = 200
KODE_TIDAK_DITEMUKAN = 404

# Jadwal contoh rekaan untuk satu hari praktik.
JADWAL_CONTOH = [
  {"dokter": "dr. A, Sp.PD", "poli": "Penyakit Dalam", "jam": "08.00-12.00"},
  {"dokter": "dr. B, Sp.A", "poli": "Anak", "jam": "13.00-16.00"},
]


class PenanganJadwal(BaseHTTPRequestHandler):
  """Menjawab dua alamat: /jadwal untuk data dan /sehat untuk pemeriksaan.

  Alamat /sehat dipakai Kubernetes (liveness probe) untuk memutuskan apakah
  container perlu dimulai ulang. Bila alamat ini berhenti menjawab,
  Kubernetes mengganti container tanpa menunggu petugas.
  """

  def do_GET(self):
    """Mengirim jadwal atau status sehat. Alamat lain dijawab kode 404."""
    if self.path == "/sehat":
      self.kirim_json(KODE_BERHASIL, {"status": "sehat"})
    elif self.path == "/jadwal":
      isi = {"fasilitas": NAMA_FASILITAS, "jadwal": JADWAL_CONTOH}
      self.kirim_json(KODE_BERHASIL, isi)
    else:
      galat = {"galat": "alamat tidak dikenal"}
      self.kirim_json(KODE_TIDAK_DITEMUKAN, galat)

  def kirim_json(self, kode_status, isi):
    """Menulis jawaban JSON. Dipisah agar setiap alamat berformat sama."""
    tersandi = json.dumps(isi, ensure_ascii=False).encode("utf-8")
    self.send_response(kode_status)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.send_header("Content-Length", str(len(tersandi)))
    self.end_headers()
    self.wfile.write(tersandi)


def jalankan():
  """Menyalakan server. Log ke stdout agar terbaca oleh kubectl logs."""
  alamat = (ALAMAT_SEMUA_ANTARMUKA, PORT)
  server = HTTPServer(alamat, PenanganJadwal)
  print(f"Layanan {NAMA_FASILITAS} berjalan di port {PORT}", flush=True)
  server.serve_forever()


if __name__ == "__main__":
  jalankan()
