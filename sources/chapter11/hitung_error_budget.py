# Kalkulator error budget untuk Aktivitas dan Latihan 1 Bab 11. Contoh pemakaian:
# python hitung_error_budget.py --target 99.5 99.9 --volume 28000 --gagal 9 --total 125
"""Menghitung error budget dan laju pembakaran dari target SLO.

Angka yang dihasilkan dipakai untuk mengisi templat SLO dan lembar Latihan 1. Jendela
dihitung dalam menit kalender, sedangkan anggaran berbasis permintaan dihitung dari
perkiraan volume dalam jendela yang sama. Keluaran memakai koma desimal agar dapat
disalin langsung ke dokumen berbahasa Indonesia.
"""
import argparse

MENIT_PER_JAM = 60
JAM_PER_HARI = 24
HARI_PER_TAHUN = 365

# Nilai bawaan mengikuti angka pemesanan Medikara+ di Bab 11.
HARI_JENDELA_BAWAAN = 30
VOLUME_BAWAAN = 28_000
TARGET_BAWAAN = [99.5, 99.9]


def anggaran_persen(target_persen):
  """Mengembalikan error budget dalam persen; target 99,5 menghasilkan 0,5."""
  return 100.0 - target_persen


def menit_diizinkan(target_persen, jumlah_hari):
  """Menghitung menit tidak tersedia yang masih memenuhi SLO dalam jendela itu."""
  total_menit = jumlah_hari * JAM_PER_HARI * MENIT_PER_JAM
  return total_menit * anggaran_persen(target_persen) / 100.0


def gagal_diizinkan(target_persen, volume):
  """Menghitung jumlah permintaan gagal yang masih memenuhi SLO."""
  return volume * anggaran_persen(target_persen) / 100.0


def laju_pembakaran(jumlah_gagal, jumlah_total, target_persen):
  """Membandingkan proporsi gagal teramati dengan proporsi gagal yang diizinkan.

  Nilai 1 berarti anggaran habis tepat di akhir jendela. Nilai 14,4 pada jendela
  30 hari berarti anggaran habis dalam sekitar 50 jam bila laju itu berlanjut.
  """
  if jumlah_total == 0:
    return 0.0
  proporsi_gagal = jumlah_gagal / jumlah_total
  return proporsi_gagal / (anggaran_persen(target_persen) / 100.0)


def format_angka(nilai, jumlah_desimal=2):
  """Menulis angka dengan koma desimal dan titik ribuan, sesuai kebiasaan Indonesia."""
  teks = f"{nilai:,.{jumlah_desimal}f}"
  return teks.replace(",", "_").replace(".", ",").replace("_", ".")


def format_durasi(menit):
  """Mengubah menit menjadi jam dan menit agar mudah dibaca manajemen."""
  jam = int(menit // MENIT_PER_JAM)
  sisa_menit = menit - jam * MENIT_PER_JAM
  return f"{jam} jam {format_angka(sisa_menit, 1)} menit"


def baca_argumen():
  """Membaca argumen baris perintah; semua argumen punya nilai bawaan."""
  parser = argparse.ArgumentParser(description="Kalkulator error budget Bab 11")
  parser.add_argument("--target", type=float, nargs="+", default=TARGET_BAWAAN,
                      help="target SLO dalam persen, misalnya 99.5")
  parser.add_argument("--hari", type=int, default=HARI_JENDELA_BAWAAN,
                      help="panjang jendela SLO dalam hari")
  parser.add_argument("--volume", type=int, default=VOLUME_BAWAAN,
                      help="perkiraan jumlah permintaan dalam satu jendela")
  parser.add_argument("--gagal", type=int,
                      help="jumlah permintaan gagal dalam selang yang diamati")
  parser.add_argument("--total", type=int,
                      help="jumlah seluruh permintaan dalam selang yang diamati")
  return parser.parse_args()


def cetak_anggaran(target, argumen):
  """Mencetak satu baris ringkasan untuk satu target."""
  menit_jendela = menit_diizinkan(target, argumen.hari)
  menit_tahun = menit_diizinkan(target, HARI_PER_TAHUN)
  print(f"Target {format_angka(target, 3)} persen")
  print(f"  error budget        : {format_angka(anggaran_persen(target), 3)} persen")
  print(f"  per {argumen.hari} hari         : {format_angka(menit_jendela)} menit"
        f" ({format_durasi(menit_jendela)})")
  print(f"  per tahun           : {format_angka(menit_tahun)} menit"
        f" ({format_durasi(menit_tahun)})")
  jumlah_gagal = gagal_diizinkan(target, argumen.volume)
  print(f"  gagal diizinkan     : {format_angka(jumlah_gagal, 0)}"
        f" dari {format_angka(argumen.volume, 0)} permintaan")


def cetak_laju(target, argumen):
  """Mencetak laju pembakaran dan sisa waktu sampai anggaran habis."""
  laju = laju_pembakaran(argumen.gagal, argumen.total, target)
  jam_jendela = argumen.hari * JAM_PER_HARI
  print(f"  laju pembakaran     : {format_angka(laju, 1)}")
  if laju > 0:
    print(f"  anggaran habis dalam: {format_angka(jam_jendela / laju, 1)} jam"
          " bila laju ini berlanjut")


def main():
  """Menjalankan perhitungan untuk setiap target yang diminta."""
  argumen = baca_argumen()
  for target in argumen.target:
    cetak_anggaran(target, argumen)
    if argumen.gagal is not None and argumen.total:
      cetak_laju(target, argumen)
    print()


if __name__ == "__main__":
  main()
