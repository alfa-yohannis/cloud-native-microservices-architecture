# Sumber Bab 02

Berkas pendukung Bab 2, Model Layanan, Model Penerapan, dan Lokasi Data. Aktivitas bab ini
menghasilkan matriks kendala penempatan *workload* untuk tonggak capstone C1. Kasus
Medikara Health di dalam berkas ini fiktif.

| Berkas | Kegunaan |
| --- | --- |
| `templat-matriks-penempatan-workload.xlsx` | Templat matriks Aktivitas. Lembar Petunjuk berisi langkah kerja dan aturan etika, lembar Matriks berisi lima baris contoh Medikara dan 12 baris kosong dengan daftar pilihan, lembar Pilihan berisi nilai yang boleh dipilih. |
| `ringkasan-regulasi-lokasi-data.md` | Ringkasan PP 71/2019, Permenkominfo 5/2020, PP 28/2024, Permenkes 24/2022, UU 27/2022, dan PP 33/2026 untuk Aktivitas dan Latihan 2, ditutup dengan daftar periksa per *workload*. |
| `lembar-latihan-bab02.md` | Lembar isian kosong Latihan 1 sampai 3. |
| `cek-zona-region.sh` | Pendalaman teknis (opsional): membaca status *region* Jakarta, nama zona, dan katalog layanan AWS serta zona Google Cloud. Hanya membaca katalog, tidak membuat sumber daya berbayar. Jalankan dengan `bash cek-zona-region.sh` setelah AWS CLI dan gcloud login. |
| `bandingkan_katalog_region.py` | Pendalaman teknis (opsional): membandingkan dua daftar layanan (satu nama per baris) dan mencetak layanan yang belum tersedia di *region* sasaran. Jalankan dengan `python bandingkan_katalog_region.py layanan-aws-us-east-1.txt layanan-aws-ap-southeast-3.txt`. |

Status regulasi diperiksa pada 30 Oktober 2026. Ringkasan regulasi bukan nasihat hukum; teks
resmi setiap aturan dicek ulang di JDIH sebelum dikutip di laporan capstone.
