# Sumber Bab 07

Berkas pendukung Bab 07, Monolit, Modular Monolith, dan Microservices. Seluruh
angka di dalamnya rekaan untuk kasus fiktif Medikara Health. Berkas dipakai pada
Aktivitas "Diagnosis Arsitektur dan ADR Pertama", pada kotak pendalaman teknis,
dan pada Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `lembar-diagnosis-coupling.xlsx` | Lembar diagnosis aplikasi inti. Lembar "Contoh Medikara" berisi angka Tabel 7.4 di naskah (perubahan dan gangguan per modul SIMRS RS Jakarta, serta pasangan modul yang berubah bersama). Lembar "Isian Tim" dipakai untuk aplikasi pilihan tim. Kolom derajat dihitung otomatis. |
| `contoh-riwayat-perubahan.csv` | Contoh 40 permintaan perubahan SIMRS RS Jakarta, Januari sampai Maret 2025. Setiap baris mencatat bagian peminta dan modul yang diubah. |
| `hitung-coupling.py` | Skrip Python (pustaka standar saja) untuk pendalaman teknis: menghitung perubahan per modul, persentase perubahan lintas modul, dan pasangan modul yang paling sering berubah bersama. |
| `templat-adr.md` | Templat ADR (*Architecture Decision Record*) dengan bagian status, konteks, opsi, keputusan, konsekuensi, syarat peninjauan ulang, dan daftar periksa sebelum diajukan. |
| `daftar-periksa-c2.md` | Daftar periksa penggabungan artefak Bab 04 sampai Bab 07 menjadi berkas tonggak C2 untuk tinjauan menjelang UTS. |

Cara menjalankan skrip:

```bash
cd sources/chapter07
python hitung-coupling.py contoh-riwayat-perubahan.csv
```

Untuk aplikasi tim, buat berkas dengan kolom yang sama (`id_perubahan`,
`tanggal`, `peminta`, `modul_diubah`, `ringkasan`). Kolom `modul_diubah` memakai
titik koma sebagai pemisah antarmodul. Baris pertama berkas contoh adalah
komentar yang diawali `#`; saat dibuka di *spreadsheet*, baris itu boleh dihapus.

Data riwayat perubahan dari organisasi nyata dipakai seizin organisasi. Nama
orang dan data pasien dihapus sebelum berkas dibagikan ke anggota tim.
