# Sumber Bab 03

Berkas pendukung Bab 03, Ekonomi Cloud, FinOps, dan Keberlanjutan. Seluruh
angka di dalamnya rekaan untuk kasus fiktif Medikara Health, kecuali disebut
lain. Berkas dipakai pada Aktivitas "Model Biaya Awal dan Sasaran Nilai Cloud"
dan pada Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-tco-sederhana.xlsx` | Templat TCO kasar lima tahun. Lembar "Contoh SIMRS Bekasi" berisi angka Tabel 3.3 di naskah; lembar "Isian Tim" dipakai untuk *workload* pilihan tim. Total dan biaya per unit dihitung otomatis. |
| `contoh-tagihan-focus.csv` | Contoh tagihan satu bulan (Agustus 2026) berformat FOCUS, berisi sebagian kolom spesifikasi. Ada baris bertag, baris tanpa tag, baris harga komitmen, baris kapasitas *spot*, dan satu baris pembelian komitmen. |
| `olah-tagihan-focus.py` | Skrip Python (pustaka standar saja) untuk pendalaman teknis: mengelompokkan `EffectiveCost` per tag layanan dan lingkungan, lalu menghitung biaya per janji temu dan per hasil pemeriksaan. |
| `lembar-sasaran-nilai.md` | Lembar kerja metrik biaya per unit dan sasaran nilai *cloud*, dengan contoh terisi dan isian kosong untuk tim. |

Cara menjalankan skrip:

```bash
cd sources/chapter03
python olah-tagihan-focus.py contoh-tagihan-focus.csv
```

Baris pertama berkas CSV adalah komentar yang diawali `#`. Saat dibuka di
*spreadsheet*, baris itu boleh dihapus agar baris judul kolom berada di atas.
