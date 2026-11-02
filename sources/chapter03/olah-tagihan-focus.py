# Kegunaan: mengelompokkan biaya tagihan FOCUS per tag dan menghitung biaya per unit.
# Cara memakai: python olah-tagihan-focus.py contoh-tagihan-focus.csv
"""Pengolah contoh tagihan berformat FOCUS untuk Aktivitas Bab 03.

Skrip ini sengaja hanya memakai pustaka standar Python, sehingga dapat
dijalankan tanpa memasang paket tambahan. Hasilnya dua ringkasan: biaya per
pasangan tag (layanan, lingkungan) dan biaya per unit bisnis tiap layanan.
"""

import csv
import json
import sys
from collections import defaultdict

# Kolom yang dijumlahkan. EffectiveCost dipilih karena sudah menyebarkan
# biaya pembelian komitmen ke pemakaiannya. Bila BilledCost yang dipakai,
# seluruh biaya komitmen jatuh ke baris pembelian yang tidak bertag.
KOLOM_BIAYA = "EffectiveCost"

# Label pengganti untuk baris tanpa tag. Dipisahkan agar biaya yang belum
# punya pemilik tetap terlihat, bukan tenggelam di dalam total.
TANPA_TAG = "(tanpa-tag)"

# Baris yang diawali tanda ini adalah komentar berkas, bukan data.
PENANDA_KOMENTAR = "#"

# Jumlah unit bisnis per layanan pada periode tagihan yang sama.
# Angka rekaan kasus Medikara Health; ganti dengan data organisasi sendiri.
UNIT_PER_LAYANAN = {
  "medikara-plus": ("janji temu", 28000),
  "lab-rujukan": ("hasil pemeriksaan", 52000),
}


def format_rupiah(nilai):
  """Menulis angka dengan titik ribuan, sesuai kebiasaan penulisan rupiah."""
  return "Rp" + f"{nilai:,.0f}".replace(",", ".")


def baca_tag(teks_tag):
  """Mengubah isi kolom Tags (teks JSON) menjadi dict.

  Kolom kosong dikembalikan sebagai dict kosong, sehingga baris tanpa tag
  tetap terhitung dan jatuh ke kelompok TANPA_TAG.
  """
  if not teks_tag:
    return {}
  return json.loads(teks_tag)


def baris_data(berkas):
  """Melewati baris komentar agar csv.DictReader membaca header yang benar."""
  for baris in berkas:
    if not baris.startswith(PENANDA_KOMENTAR):
      yield baris


def kelompokkan_biaya(jalur_berkas):
  """Menjumlahkan biaya per pasangan (layanan, lingkungan)."""
  total = defaultdict(float)
  with open(jalur_berkas, newline="", encoding="utf-8") as berkas:
    for baris in csv.DictReader(baris_data(berkas)):
      tag = baca_tag(baris["Tags"])
      layanan = tag.get("layanan", TANPA_TAG)
      lingkungan = tag.get("lingkungan", TANPA_TAG)
      total[(layanan, lingkungan)] += float(baris[KOLOM_BIAYA])
  return total


def nilai_biaya(pasangan):
  """Kunci pengurutan: biaya terbesar lebih dulu, agar pemborosan cepat terlihat."""
  return -pasangan[1]


def cetak_ringkasan(total):
  """Mencetak biaya per pasangan tag, dari yang terbesar."""
  urutan = sorted(total.items(), key=nilai_biaya)
  for (layanan, lingkungan), biaya in urutan:
    print(f"{layanan:20} {lingkungan:14} {format_rupiah(biaya):>16}")
  print(f"{'TOTAL':35} {format_rupiah(sum(total.values())):>16}")


def cetak_biaya_per_unit(total):
  """Menghitung biaya per unit dari seluruh lingkungan satu layanan.

  Lingkungan pengembangan ikut dihitung karena keberadaannya hanya untuk
  melayani layanan tersebut. Mengabaikannya membuat biaya per unit tampak
  lebih murah daripada kenyataannya.
  """
  for layanan, (nama_unit, jumlah_unit) in UNIT_PER_LAYANAN.items():
    biaya_layanan = sum(
      biaya for (nama, lingkungan), biaya in total.items() if nama == layanan
    )
    biaya_per_unit = biaya_layanan / jumlah_unit
    print(f"{layanan}: {format_rupiah(biaya_per_unit)} per {nama_unit}")


def main():
  """Membaca jalur berkas dari argumen, lalu mencetak dua ringkasan."""
  if len(sys.argv) != 2:
    print("Pemakaian: python olah-tagihan-focus.py <berkas-focus.csv>")
    sys.exit(1)
  total = kelompokkan_biaya(sys.argv[1])
  cetak_ringkasan(total)
  print()
  cetak_biaya_per_unit(total)


if __name__ == "__main__":
  main()
