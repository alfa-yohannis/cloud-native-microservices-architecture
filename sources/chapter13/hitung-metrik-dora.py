# Kegunaan: menghitung metrik DORA per aplikasi dari riwayat deployment.
# Cara pakai:
#   python hitung-metrik-dora.py contoh-riwayat-deployment.csv [jumlah_bulan]
"""Menghitung metrik pengiriman DORA dari catatan deployment.

Metrik dihitung dari data, bukan dari kesan, agar anggapan seperti "rilis yang
jarang lebih aman" dapat diuji. Skrip ini dipakai pada Latihan 1 dan Aktivitas
Bab 13. Hanya pustaka standar Python yang dipakai, sehingga skrip dapat
dijalankan tanpa memasang paket tambahan.
"""

import csv
import statistics
import sys
from collections import defaultdict

# Lama periode pengamatan bawaan. Data contoh mencakup Januari sampai Desember
# 2025; frekuensi per bulan akan salah bila angka ini tidak sesuai data.
BULAN_PENGAMATAN_BAWAAN = 12

# Nilai kolom yang menandai deployment gagal dan deployment tidak terencana.
NILAI_BUTUH_PERBAIKAN = "ya"
JENIS_DARURAT = "darurat"
JENIS_TERJADWAL = "terjadwal"

# Peluang satu perubahan menimbulkan masalah. Angka ini asumsi pengajaran,
# bukan temuan DORA; dipakai untuk menunjukkan pengaruh ukuran rilis.
PELUANG_MASALAH_PER_PERUBAHAN = 0.01

MENIT_PER_JAM = 60
PERSEN = 100


def baca_riwayat(jalur_berkas):
  """Membaca CSV dan mengelompokkan deployment menurut nama aplikasi.

  Baris yang diawali '#' dilewati agar berkas boleh memuat keterangan di
  bagian atas. Angka diubah ke int di sini supaya fungsi lain tidak perlu
  mengulang konversi.
  """
  per_aplikasi = defaultdict(list)
  with open(jalur_berkas, newline="", encoding="utf-8") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith("#"))
    for rekaman in csv.DictReader(baris_data):
      per_aplikasi[rekaman["aplikasi"]].append({
        "jenis": rekaman["jenis"].strip(),
        "jumlah_perubahan": int(rekaman["jumlah_perubahan"]),
        "lead_time_hari": int(rekaman["lead_time_hari"]),
        "gagal": rekaman["butuh_perbaikan"].strip() == NILAI_BUTUH_PERBAIKAN,
        "menit_pemulihan": int(rekaman["menit_pemulihan"]),
      })
  return per_aplikasi


def lead_time_rata_rata(daftar_deployment):
  """Rata-rata lead time per perubahan, ditimbang jumlah perubahan.

  Penimbangan dipakai karena DORA mengukur lead time per perubahan. Tanpa
  penimbangan, satu perbaikan darurat berisi satu perubahan akan berbobot
  sama dengan rilis triwulanan berisi enam puluh perubahan.
  """
  total_perubahan = sum(item["jumlah_perubahan"] for item in daftar_deployment)
  total_hari = sum(
    item["jumlah_perubahan"] * item["lead_time_hari"]
    for item in daftar_deployment
  )
  return total_hari / total_perubahan


def peluang_rilis_bermasalah(jumlah_perubahan):
  """Peluang minimal satu perubahan dalam satu rilis menimbulkan masalah.

  Rumusnya 1 - (1 - p) pangkat n. Akibatnya, rilis besar hampir pasti
  membawa masalah walaupun setiap perubahan dibuat dengan hati-hati.
  """
  peluang_bersih = (1 - PELUANG_MASALAH_PER_PERUBAHAN) ** jumlah_perubahan
  return 1 - peluang_bersih


def hitung_metrik(daftar_deployment, jumlah_bulan):
  """Menghitung metrik DORA dan ukuran rilis untuk satu aplikasi."""
  jumlah = len(daftar_deployment)
  gagal = [item for item in daftar_deployment if item["gagal"]]
  darurat = [item for item in daftar_deployment if item["jenis"] == JENIS_DARURAT]
  terjadwal = [
    item["jumlah_perubahan"] for item in daftar_deployment
    if item["jenis"] == JENIS_TERJADWAL
  ]
  menit_pulih = [item["menit_pemulihan"] for item in gagal]
  ukuran_rilis = statistics.mean(terjadwal) if terjadwal else 0
  return {
    "jumlah_deployment": jumlah,
    "jumlah_darurat": len(darurat),
    "per_bulan": jumlah / jumlah_bulan,
    "lead_time_hari": lead_time_rata_rata(daftar_deployment),
    "jumlah_gagal": len(gagal),
    "tingkat_gagal": PERSEN * len(gagal) / jumlah,
    "tingkat_ulang": PERSEN * len(darurat) / jumlah,
    "pulih_jam": statistics.median(menit_pulih) / MENIT_PER_JAM if gagal else 0,
    "ukuran_rilis": ukuran_rilis,
    "peluang_masalah": PERSEN * peluang_rilis_bermasalah(round(ukuran_rilis)),
  }


def cetak_laporan(nama_aplikasi, metrik):
  """Mencetak ringkasan yang siap disalin ke lembar Latihan 1."""
  print(f"== {nama_aplikasi} ==")
  print(f"  Deployment: {metrik['jumlah_deployment']} "
        f"({metrik['jumlah_darurat']} darurat), "
        f"{metrik['per_bulan']:.2f} per bulan")
  print(f"  Lead time perubahan rata-rata: {metrik['lead_time_hari']:.1f} hari")
  print(f"  Tingkat kegagalan perubahan: {metrik['jumlah_gagal']} dari "
        f"{metrik['jumlah_deployment']} ({metrik['tingkat_gagal']:.0f}%)")
  print(f"  Tingkat pengerjaan ulang: {metrik['tingkat_ulang']:.0f}%")
  print(f"  Waktu pemulihan median: {metrik['pulih_jam']:.1f} jam")
  print(f"  Perubahan per rilis terjadwal: {metrik['ukuran_rilis']:.1f}")
  print(f"  Peluang rilis bermasalah (asumsi 1%): "
        f"{metrik['peluang_masalah']:.1f}%")


def main():
  """Titik masuk skrip; jalur berkas wajib diberikan agar sumber data jelas."""
  if len(sys.argv) not in (2, 3):
    print("Pemakaian: python hitung-metrik-dora.py <berkas.csv> [jumlah_bulan]")
    sys.exit(1)
  jumlah_bulan = BULAN_PENGAMATAN_BAWAAN
  if len(sys.argv) == 3:
    jumlah_bulan = int(sys.argv[2])
  per_aplikasi = baca_riwayat(sys.argv[1])
  for nama_aplikasi, daftar_deployment in per_aplikasi.items():
    cetak_laporan(nama_aplikasi, hitung_metrik(daftar_deployment, jumlah_bulan))


if __name__ == "__main__":
  main()
