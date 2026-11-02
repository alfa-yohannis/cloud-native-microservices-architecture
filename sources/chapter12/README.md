# Sumber Bab 12

Berkas pendukung Bab 12, Resiliensi dan Disaster Recovery. Seluruh angka di
dalamnya rekaan untuk kasus fiktif Medikara Health. Berkas dipakai pada
Aktivitas "Rencana Resiliensi dan DR", pada kotak pendalaman teknis, dan pada
Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-analisis-dampak-bisnis.xlsx` | Templat analisis dampak bisnis dan pemilihan strategi DR. Lembar "Contoh Medikara" berisi angka Kasus Medikara di naskah (rekam medis elektronik, Medikara+, ERP keuangan). Lembar "Isian Tim" dipakai untuk layanan kritis tim dari Bab 11. Lembar "Profil Strategi" memuat perkiraan kasar RTO, RPO, dan rasio biaya empat strategi. Biaya DR, perkiraan kerugian tahunan, dan kecocokan target dihitung otomatis. |
| `templat-rencana-dr.md` | Templat rencana resiliensi dan DR: hasil analisis dampak bisnis, pola resiliensi per ketergantungan, arsitektur DR, kriteria deklarasi bencana, peran, urutan pemulihan, jadwal uji, dan daftar periksa sebelum diajukan. |
| `skenario-game-day.md` | Contoh skenario latihan meja "*region* utama tidak tersedia selama empat jam" untuk Medikara, templat skenario tim, lembar evaluasi, dan syarat aman sebelum pemindahan nyata. |
| `simulasi-circuit-breaker.py` | Skrip Python (pustaka standar saja) untuk pendalaman teknis: membandingkan pemanggil tanpa dan dengan *circuit breaker* ketika layanan pihak ketiga gangguan selama 60 detik simulasi. |
| `bandingkan-strategi-dr.py` | Skrip Python (pustaka standar saja) untuk Latihan 3: menghitung biaya DR, perkiraan kerugian tahunan, dan strategi termurah yang memenuhi RTO dan RPO untuk setiap layanan. |

Cara menjalankan skrip:

```bash
cd sources/chapter12
python simulasi-circuit-breaker.py
python bandingkan-strategi-dr.py
python bandingkan-strategi-dr.py data-tim.csv
```

Berkas `data-tim.csv` dibuat sendiri oleh tim dengan kolom `layanan`,
`kerugian_per_jam_juta`, `biaya_produksi_juta`, `rto_target_jam`, dan
`rpo_target_menit`. Tanpa argumen, skrip memakai angka contoh Medikara.

Data organisasi nyata dipakai seizin organisasi dan dianonimkan. Data pribadi
pasien atau karyawan tidak dimasukkan ke templat. Skenario *game day* dengan
pemindahan nyata hanya dijalankan pada sistem milik sendiri atau sistem yang
sudah berizin tertulis.
