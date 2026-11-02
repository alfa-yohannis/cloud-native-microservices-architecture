# Kegunaan: menghitung pasangan modul yang sering berubah bersamaan dari riwayat
# permintaan perubahan. Cara pakai:
#   python hitung-coupling.py contoh-riwayat-perubahan.csv
"""Menghitung keterkaitan perubahan (change coupling) antarmodul.

Pasangan modul yang sering berubah dalam satu permintaan yang sama adalah tanda
coupling yang tidak selalu terlihat di diagram. Hasil skrip ini menjadi bahan
lembar diagnosis pada Aktivitas Bab 07. Skrip hanya memakai pustaka standar
Python agar dapat dijalankan tanpa memasang paket tambahan.
"""

import csv
import sys
from collections import Counter
from itertools import combinations

# Pemisah antarmodul di kolom modul_diubah. Titik koma dipilih agar berkas tetap
# terbaca sebagai CSV biasa yang memakai koma sebagai pemisah kolom.
PEMISAH_MODUL = ";"

# Pasangan yang berubah bersama kurang dari angka ini dianggap kebetulan, sehingga
# tidak dicetak agar daftar tidak penuh derau.
MINIMUM_PERUBAHAN_BERSAMA = 3

# Jumlah pasangan teratas yang dicetak; cukup untuk dibahas dalam satu rapat tim.
JUMLAH_PASANGAN_DITAMPILKAN = 5


def baca_riwayat(jalur_berkas):
  """Membaca CSV dan mengembalikan daftar himpunan modul per perubahan.

  Baris yang diawali '#' dilewati agar berkas boleh memuat keterangan di bagian
  atas. Himpunan dipakai supaya modul yang tertulis dua kali tidak dihitung ganda.
  """
  daftar_perubahan = []
  with open(jalur_berkas, newline="", encoding="utf-8") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith("#"))
    for rekaman in csv.DictReader(baris_data):
      daftar_modul = rekaman["modul_diubah"].split(PEMISAH_MODUL)
      daftar_perubahan.append({nama.strip() for nama in daftar_modul if nama.strip()})
  return daftar_perubahan


def hitung_keterkaitan(daftar_perubahan):
  """Menghitung jumlah perubahan per modul dan per pasangan modul.

  Pasangan diurutkan menurut abjad agar (a, b) dan (b, a) dihitung sebagai
  pasangan yang sama.
  """
  per_modul = Counter()
  per_pasangan = Counter()
  for modul_berubah in daftar_perubahan:
    per_modul.update(modul_berubah)
    for pasangan in combinations(sorted(modul_berubah), 2):
      per_pasangan[pasangan] += 1
  return per_modul, per_pasangan


def derajat_keterkaitan(bersama, jumlah_pertama, jumlah_kedua):
  """Persentase perubahan bersama terhadap rata-rata perubahan kedua modul.

  Rata-rata dipakai agar modul yang sangat sering berubah tidak membuat
  semua pasangannya tampak erat. Hasil di atas 50 persen layak dibahas tim.
  """
  rata_rata = (jumlah_pertama + jumlah_kedua) / 2
  return round(100 * bersama / rata_rata)


def cetak_laporan(daftar_perubahan, per_modul, per_pasangan):
  """Mencetak ringkasan yang siap disalin ke lembar diagnosis."""
  lintas_modul = sum(1 for modul in daftar_perubahan if len(modul) > 1)
  persen_lintas = round(100 * lintas_modul / len(daftar_perubahan))
  print(f"Jumlah perubahan: {len(daftar_perubahan)}")
  print(f"Menyentuh lebih dari satu modul: {lintas_modul} ({persen_lintas}%)")
  print("Perubahan per modul:")
  for nama, jumlah in per_modul.most_common():
    print(f"  {nama}: {jumlah}")
  print("Pasangan yang paling sering berubah bersama:")
  teratas = [
    (pasangan, jumlah) for pasangan, jumlah in per_pasangan.most_common()
    if jumlah >= MINIMUM_PERUBAHAN_BERSAMA
  ][:JUMLAH_PASANGAN_DITAMPILKAN]
  for (pertama, kedua), bersama in teratas:
    derajat = derajat_keterkaitan(bersama, per_modul[pertama], per_modul[kedua])
    print(f"  {pertama} + {kedua}: {bersama} kali, derajat {derajat}%")


def main():
  """Titik masuk skrip; jalur berkas wajib diberikan agar sumber data jelas."""
  if len(sys.argv) != 2:
    print("Pemakaian: python hitung-coupling.py <berkas-riwayat.csv>")
    sys.exit(1)
  daftar_perubahan = baca_riwayat(sys.argv[1])
  per_modul, per_pasangan = hitung_keterkaitan(daftar_perubahan)
  cetak_laporan(daftar_perubahan, per_modul, per_pasangan)


if __name__ == "__main__":
  main()
