# Mencocokkan tabel basis data dengan bounded context hasil lokakarya EventStorming.
# Jalankan: python cocokkan-tabel-konteks.py contoh-akses-tabel-simrs.csv
"""Mencocokkan tabel basis data aplikasi lama dengan bounded context.

Skrip ini dipakai pada pendalaman teknis Bab 06. Masukannya daftar akses modul
ke tabel, lengkap dengan bounded context tempat modul itu dikelompokkan setelah
lokakarya EventStorming. Keluarannya dua daftar:

1. Tabel yang ditulis oleh lebih dari satu bounded context. Tabel seperti ini
   belum punya pemilik tunggal, sehingga menjadi titik paling sulit saat sistem
   dipecah menjadi layanan.
2. Pembacaan lintas konteks, yaitu konteks yang membaca tabel milik konteks
   lain. Setiap pembacaan ini kelak perlu diganti dengan API atau event.

Hanya pustaka standar Python yang dipakai, agar skrip dapat dijalankan tanpa
instalasi tambahan.
"""

import csv
import sys
from collections import defaultdict

# Nilai kolom "akses" pada berkas CSV.
AKSES_TULIS = "tulis"
AKSES_BACA = "baca"

# Satu tabel idealnya hanya ditulis oleh satu bounded context.
BATAS_PENULIS = 1

# Baris yang diawali tanda ini adalah komentar, bukan data.
PENANDA_KOMENTAR = "#"


def baca_akses(jalur_berkas):
  """Membaca daftar akses dan melewati baris komentar.

  Baris komentar dibuang lebih dahulu agar csv.DictReader membaca baris judul
  kolom yang benar. Akibatnya, berkas boleh diberi keterangan di baris awal.
  """
  with open(jalur_berkas, newline="", encoding="utf-8") as berkas:
    baris_data = [
      baris for baris in berkas if not baris.startswith(PENANDA_KOMENTAR)
    ]
  return list(csv.DictReader(baris_data))


def kelompokkan_akses(daftar_akses):
  """Mengumpulkan konteks penulis dan pembaca untuk setiap tabel.

  Himpunan dipakai agar satu konteks yang punya beberapa modul penulis tidak
  terhitung dua kali. Dua modul dalam satu konteks memang boleh berbagi tabel.
  """
  penulis = defaultdict(set)
  pembaca = defaultdict(set)
  for akses in daftar_akses:
    tabel = akses["tabel"]
    if akses["akses"] == AKSES_TULIS:
      penulis[tabel].add(akses["konteks"])
    elif akses["akses"] == AKSES_BACA:
      pembaca[tabel].add(akses["konteks"])
  return penulis, pembaca


def kunci_urutan_rebutan(pasangan):
  """Kunci urutan: penulis terbanyak lebih dahulu, lalu nama tabel.

  Tabel dengan penulis terbanyak paling mahal untuk dipisahkan, sehingga perlu
  dibahas lebih dahulu dalam rapat tim.
  """
  tabel, konteks = pasangan
  return (-len(konteks), tabel)


def cari_tabel_rebutan(penulis):
  """Mengembalikan tabel yang ditulis lebih dari satu konteks, sudah terurut."""
  rebutan = [
    (tabel, konteks)
    for tabel, konteks in penulis.items()
    if len(konteks) > BATAS_PENULIS
  ]
  return sorted(rebutan, key=kunci_urutan_rebutan)


def cari_baca_lintas(penulis, pembaca):
  """Mengembalikan pasangan (konteks pembaca, tabel) yang melintasi batas.

  Pembacaan dianggap lintas konteks bila pembacanya bukan salah satu penulis
  tabel itu. Pembacaan ini kelak diganti dengan API atau event dari pemilik.
  """
  lintas = []
  for tabel, daftar_pembaca in pembaca.items():
    for konteks in sorted(daftar_pembaca - penulis.get(tabel, set())):
      lintas.append((konteks, tabel))
  return sorted(lintas)


def cetak_laporan(penulis, pembaca):
  """Mencetak ringkasan agar mudah disalin ke lembar kerja tim."""
  semua_tabel = set(penulis) | set(pembaca)
  rebutan = cari_tabel_rebutan(penulis)
  print("Tabel yang ditulis lebih dari satu bounded context:")
  for tabel, konteks in rebutan:
    print(f"  {tabel}: {', '.join(sorted(konteks))}")
  jumlah_satu_pemilik = len(semua_tabel) - len(rebutan)
  print(f"Tabel dengan satu pemilik: {jumlah_satu_pemilik} dari {len(semua_tabel)}")
  lintas = cari_baca_lintas(penulis, pembaca)
  print(f"Pembacaan lintas konteks: {len(lintas)}")
  for konteks, tabel in lintas:
    print(f"  {konteks} membaca {tabel}")


def main():
  """Titik masuk skrip; menolak dijalankan tanpa nama berkas masukan."""
  if len(sys.argv) != 2:
    print("Pemakaian: python cocokkan-tabel-konteks.py <berkas-akses.csv>")
    sys.exit(1)
  penulis, pembaca = kelompokkan_akses(baca_akses(sys.argv[1]))
  cetak_laporan(penulis, pembaca)


if __name__ == "__main__":
  main()
