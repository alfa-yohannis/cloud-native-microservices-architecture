# Diagram Bab

Gambar aktif pada modul dan slide adalah diagram PNG berlabel. Setiap panah menyatakan alur atau relasi yang tertulis pada labelnya. Diagram disusun dari konsep, batasan, dan kasus pada naskah masing-masing bab, bukan hanya dari judul bab. Seluruh diagram ini dibuat tanpa TikZ.

PNG dipakai oleh LaTeX; SVG menyimpan versi vektor. Spesifikasi komponen, hubungan, catatan batas, dan dasar pemilihan terdapat pada [chapter-diagrams.json](chapter-diagrams.json). Kotak memakai notasi generik, bukan klaim konformansi ArchiMate atau reproduksi gambar standar.

| Bab | Isi diagram | PNG | SVG |
| --- | --- | --- | --- |
| 01 | Perjalanan permintaan janji temu dan ketergantungannya | [gambar](ch01-diagram-konsep.png) | [vektor](ch01-diagram-konsep.svg) |
| 02 | Memilih model cloud berdasarkan workload dan kendali | [gambar](ch02-diagram-konsep.png) | [vektor](ch02-diagram-konsep.svg) |
| 03 | FinOps: dari data biaya ke keputusan berulang | [gambar](ch03-diagram-konsep.png) | [vektor](ch03-diagram-konsep.svg) |
| 04 | Kesiapan dan fondasi mendahului gelombang migrasi | [gambar](ch04-diagram-konsep.png) | [vektor](ch04-diagram-konsep.svg) |
| 05 | Aplikasi stateless memisahkan proses dari data persisten | [gambar](ch05-diagram-konsep.png) | [vektor](ch05-diagram-konsep.svg) |
| 06 | Dari peristiwa bisnis ke batas model domain | [gambar](ch06-diagram-konsep.png) | [vektor](ch06-diagram-konsep.svg) |
| 07 | Batas modul dipilih sebelum distribusi layanan | [gambar](ch07-diagram-konsep.png) | [vektor](ch07-diagram-konsep.svg) |
| 08 | Kubernetes merekonsiliasi keadaan yang diinginkan | [gambar](ch08-diagram-konsep.png) | [vektor](ch08-diagram-konsep.svg) |
| 09 | Penyampaian event dan penanganan duplikasi | [gambar](ch09-diagram-konsep.png) | [vektor](ch09-diagram-konsep.svg) |
| 10 | Transaksi lokal, outbox, dan kompensasi saga | [gambar](ch10-diagram-konsep.png) | [vektor](ch10-diagram-konsep.svg) |
| 11 | Observabilitas menghubungkan perjalanan pengguna ke keputusan SRE | [gambar](ch11-diagram-konsep.png) | [vektor](ch11-diagram-konsep.svg) |
| 12 | Ketahanan request dan pemulihan data saling melengkapi | [gambar](ch12-diagram-konsep.png) | [vektor](ch12-diagram-konsep.svg) |
| 13 | GitOps dan platform internal memperpendek jalur perubahan | [gambar](ch13-diagram-konsep.png) | [vektor](ch13-diagram-konsep.svg) |
| 14 | Strangler memindahkan irisan layanan secara bertahap | [gambar](ch14-diagram-konsep.png) | [vektor](ch14-diagram-konsep.svg) |

## Membuat ulang

Jalankan dari akar repositori dengan Python, Matplotlib, dan Pillow:

```powershell
python tools/render-diagrams.py
python tools/render-diagrams.py --chapter 1 5
```

Font Titillium Web dibaca dari `module/fonts/`. PNG RGB maksimum 500 KiB; SVG menyimpan huruf sebagai path agar tampilannya tetap sama. Ubah `chapter-diagrams.json` untuk mengubah komponen atau relasi.

JPG ilustrasi terdahulu disimpan sebagai arsip dan tidak lagi dirujuk pada gambar bab aktif. Diagram TikZ pendukung yang sudah ada tetap menjadi bagian materi.
