# Sumber Bab 04

Berkas pendukung Bab 04, Kerangka Adopsi Cloud dan Strategi Migrasi 7R. Seluruh
angka di dalamnya rekaan untuk kasus fiktif Medikara Health, kecuali disebut
lain. Berkas dipakai pada Aktivitas "Penilaian Kesiapan dan Portofolio 7R" dan
pada Latihan.

| Berkas | Kegunaan |
| --- | --- |
| `lembar-penilaian-kesiapan-caf.xlsx` | Lembar penilaian kesiapan *cloud* enam perspektif AWS CAF, tiga pertanyaan per perspektif. Lembar "Contoh Medikara" berisi skor, bukti, dan pemilik jawaban yang sama dengan naskah bab; lembar "Isian Tim" dipakai tim. Rata-rata, skor terendah, dan status terhadap batas minimal dihitung otomatis. |
| `templat-inventaris-aplikasi.xlsx` | Templat inventaris portofolio aplikasi: pemilik, pengguna, kritikalitas, teknologi, kontrak, dependensi, kondisi, usulan 7R, dan alasan satu kalimat. Lembar "Contoh Medikara" berisi delapan aplikasi dari naskah; sebaran usulan dihitung otomatis. |
| `panduan-keputusan-7r.md` | Urutan pertanyaan 7R, bukti minimal tiap usulan, aturan saat usulan diperdebatkan, dan lembar pembanding dua pilihan untuk Latihan 2. |
| `contoh-koneksi-jaringan.csv` | Contoh catatan koneksi 30 hari antaraplikasi Medikara Health, termasuk dua dependensi tersembunyi dan kolom `boleh_dipisah` yang diisi tim. |
| `kelompok-pindah.py` | Skrip Python (pustaka standar saja) untuk pendalaman teknis: menyusun kelompok pindah dari catatan koneksi dengan mencari komponen terhubung. |

Cara menjalankan skrip:

```bash
cd sources/chapter04
python kelompok-pindah.py contoh-koneksi-jaringan.csv
```

Hasil dengan data contoh: satu kelompok berisi tujuh aplikasi, karena skrip
malam dari SIMRS Jakarta ke folder bersama menyatukan kelompok SIMRS dan
kelompok ERP keuangan. Ubah nilai `boleh_dipisah` pada baris
`SIMRS Jakarta,Folder bersama` menjadi `ya` untuk melihat hasil bila skrip malam
diganti lebih dulu: kelompok itu terpecah menjadi dua.

Baris pertama berkas CSV adalah komentar yang diawali `#`. Saat dibuka di
*spreadsheet*, baris itu boleh dihapus agar baris judul kolom berada di atas.

Catatan etika: log jaringan organisasi nyata hanya dipakai seizin pemiliknya,
dengan alamat dan nama server yang dianonimkan. Jangan memindai jaringan milik
pihak lain.
