# Mengelompokkan aplikasi menjadi kelompok pindah dari catatan koneksi jaringan.
# Pemakaian: python kelompok-pindah.py contoh-koneksi-jaringan.csv
"""Membangun kelompok pindah dari catatan koneksi antaraplikasi.

Aplikasi yang saling terhubung, langsung maupun lewat aplikasi lain, sebaiknya
dipindahkan dalam gelombang yang sama. Bila dipisah, koneksinya melintasi
jaringan antara pusat data dan cloud, sehingga menjadi lambat atau putus.
Skrip ini hanya memakai pustaka standar Python.
"""

import csv
import sys
from collections import defaultdict, deque

# Koneksi yang lebih jarang dari ini dianggap derau, misalnya uji coba sekali.
MINIMUM_KONEKSI_30_HARI = 10

# Pihak luar tidak ikut dipindahkan, sehingga tidak boleh menyatukan kelompok.
PIHAK_LUAR = {"BPJS Kesehatan", "SATUSEHAT"}


def baca_koneksi(jalur_berkas):
  """Membaca baris koneksi dan membuang baris komentar di awal berkas."""
  with open(jalur_berkas, encoding="utf-8") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith("#")]
  return list(csv.DictReader(baris_data))


def koneksi_mengikat(koneksi):
  """Menentukan apakah satu koneksi memaksa kedua ujungnya pindah bersama.

  Koneksi tidak mengikat bila terlalu jarang, bila menuju pihak luar, atau
  bila tim sudah menandainya boleh dipisah, misalnya API yang memang
  dirancang untuk dipanggil lewat internet.
  """
  jumlah = int(koneksi["jumlah_koneksi_30_hari"])
  if jumlah < MINIMUM_KONEKSI_30_HARI:
    return False
  if koneksi["sumber"] in PIHAK_LUAR or koneksi["tujuan"] in PIHAK_LUAR:
    return False
  return koneksi["boleh_dipisah"].strip().lower() != "ya"


def bangun_tetangga(daftar_koneksi):
  """Menyusun daftar tetangga tanpa arah dari koneksi yang mengikat.

  Arah koneksi diabaikan karena kedua ujungnya sama-sama terganggu bila
  dipisah. Aplikasi tanpa koneksi mengikat tetap dicatat sebagai kelompok
  sendiri, sehingga kandidat Retire ikut terlihat.
  """
  tetangga = defaultdict(set)
  for koneksi in daftar_koneksi:
    sumber = koneksi["sumber"]
    tujuan = koneksi["tujuan"]
    for aplikasi in (sumber, tujuan):
      if aplikasi not in PIHAK_LUAR:
        tetangga.setdefault(aplikasi, set())
    if koneksi_mengikat(koneksi):
      tetangga[sumber].add(tujuan)
      tetangga[tujuan].add(sumber)
  return tetangga


def cari_kelompok(tetangga):
  """Mencari komponen terhubung dengan penelusuran melebar.

  Setiap komponen adalah satu kelompok pindah. Nama diurutkan agar hasil
  setiap kali dijalankan sama dan mudah dibandingkan.
  """
  sudah_dikunjungi = set()
  daftar_kelompok = []
  for aplikasi_awal in sorted(tetangga):
    if aplikasi_awal in sudah_dikunjungi:
      continue
    kelompok = []
    antrean = deque([aplikasi_awal])
    sudah_dikunjungi.add(aplikasi_awal)
    while antrean:
      aplikasi = antrean.popleft()
      kelompok.append(aplikasi)
      for berikutnya in sorted(tetangga[aplikasi]):
        if berikutnya not in sudah_dikunjungi:
          sudah_dikunjungi.add(berikutnya)
          antrean.append(berikutnya)
    daftar_kelompok.append(sorted(kelompok))
  return daftar_kelompok


def main():
  """Mencetak kelompok pindah, dimulai dari kelompok terbesar."""
  if len(sys.argv) != 2:
    print("Pemakaian: python kelompok-pindah.py contoh-koneksi-jaringan.csv")
    sys.exit(1)
  tetangga = bangun_tetangga(baca_koneksi(sys.argv[1]))
  daftar_kelompok = cari_kelompok(tetangga)
  daftar_kelompok.sort(key=len, reverse=True)
  for nomor, kelompok in enumerate(daftar_kelompok, start=1):
    print(f"Kelompok pindah {nomor} ({len(kelompok)} aplikasi):")
    for aplikasi in kelompok:
      print(f"  - {aplikasi}")


if __name__ == "__main__":
  main()
