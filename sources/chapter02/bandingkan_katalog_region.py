# Membandingkan dua daftar layanan cloud (satu nama per baris). Pakai:
# python bandingkan_katalog_region.py layanan-pembanding.txt layanan-sasaran.txt
"""Pembanding katalog layanan antarregion milik satu penyedia.

Region yang lebih baru biasanya belum memuat seluruh layanan yang ada di
region tertua penyedia yang sama. Skrip ini menyusun selisihnya, sehingga tim
dapat memeriksa apakah layanan yang dibutuhkan sebuah workload memang tersedia
di region sasaran sebelum memutuskan lokasi data.
"""

import sys
from pathlib import Path

PENANDA_KOMENTAR = "#"
JUMLAH_ARGUMEN_WAJIB = 2


def baca_daftar_layanan(jalur_berkas):
  """Membaca nama layanan, satu per baris, sebagai himpunan.

  Baris kosong dan baris komentar dilewati agar berkas boleh diberi catatan
  tanpa merusak perbandingan. Huruf diseragamkan menjadi huruf kecil karena
  penulisan nama layanan di katalog tidak selalu konsisten. Pengodean
  utf-8-sig membuang penanda BOM dari penyunting di Windows, sehingga baris
  pertama tidak salah dibaca.
  """
  daftar = set()
  isi_berkas = Path(jalur_berkas).read_text(encoding="utf-8-sig")
  for baris in isi_berkas.splitlines():
    nama = baris.strip().lower()
    if nama and not nama.startswith(PENANDA_KOMENTAR):
      daftar.add(nama)
  return daftar


def bandingkan(layanan_pembanding, layanan_sasaran):
  """Mengembalikan layanan yang belum ada dan yang hanya ada di sasaran.

  Layanan yang hanya ada di region sasaran tetap dilaporkan, karena biasanya
  menandakan perbedaan penamaan, bukan layanan yang benar-benar baru.
  """
  belum_ada = sorted(layanan_pembanding - layanan_sasaran)
  hanya_di_sasaran = sorted(layanan_sasaran - layanan_pembanding)
  return belum_ada, hanya_di_sasaran


def cetak_bagian(judul, daftar_nama):
  """Mencetak satu bagian laporan beserta jumlahnya agar mudah disalin."""
  print(f"{judul} ({len(daftar_nama)} layanan)")
  for nama in daftar_nama:
    print(f"  - {nama}")


def main():
  """Membaca dua berkas dari argumen, lalu mencetak hasil perbandingan."""
  if len(sys.argv) != JUMLAH_ARGUMEN_WAJIB + 1:
    print("Pakai: python bandingkan_katalog_region.py PEMBANDING SASARAN")
    sys.exit(1)
  layanan_pembanding = baca_daftar_layanan(sys.argv[1])
  layanan_sasaran = baca_daftar_layanan(sys.argv[2])
  belum_ada, hanya_di_sasaran = bandingkan(layanan_pembanding, layanan_sasaran)
  print(f"Layanan di region pembanding: {len(layanan_pembanding)}")
  print(f"Layanan di region sasaran: {len(layanan_sasaran)}")
  cetak_bagian("Belum tersedia di region sasaran", belum_ada)
  cetak_bagian("Hanya ada di region sasaran", hanya_di_sasaran)


if __name__ == "__main__":
  main()
