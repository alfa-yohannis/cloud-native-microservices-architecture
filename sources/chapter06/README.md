# Sumber Bab 06

Berkas pendukung Bab 06, Domain-Driven Design dan Batas Layanan. Seluruh data
di dalamnya rekaan untuk kasus fiktif Medikara Health, kecuali disebut lain.
Berkas dipakai pada Aktivitas "Lokakarya EventStorming dan Context Map", pada
kotak pendalaman teknis, dan pada Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `panduan-fasilitasi-eventstorming.md` | Panduan fasilitator: pembagian peran, warna catatan tempel, agenda dua sesi masing-masing 120 menit, aturan main, pertanyaan pemandu, petunjuk batas *bounded context*, dan daftar periksa lokakarya daring. |
| `templat-context-map.drawio` | Templat *context map* untuk diagrams.net (draw.io). Berisi contoh kotak konteks, sistem eksternal, panah hulu-hilir berlabel pola, dan keterangan. Dipakai pada langkah 5 Aktivitas. |
| `contoh-akses-tabel-simrs.csv` | Data rekaan 34 akses dari 8 modul SIMRS rumah sakit Jakarta ke 14 tabel basis data, lengkap dengan *bounded context* setiap modul. Masukan untuk skrip pendalaman teknis. |
| `cocokkan-tabel-konteks.py` | Skrip Python (pustaka standar saja) untuk pendalaman teknis: melaporkan tabel yang ditulis lebih dari satu *bounded context* dan pembacaan lintas konteks. |

Cara menjalankan skrip:

```bash
cd sources/chapter06
python cocokkan-tabel-konteks.py contoh-akses-tabel-simrs.csv
```

Hasil dengan data contoh: 9 dari 14 tabel punya satu konteks penulis, 5 tabel
ditulis lebih dari satu konteks, dan ada 10 pembacaan lintas konteks. Angka ini
sama dengan yang dikutip di kotak pendalaman seksi "Dari Bounded Context ke
Kandidat Layanan".

Untuk organisasi nyata, daftar akses diisi dari dokumentasi aplikasi atau
wawancara dengan tim TI, seizin organisasi. Jangan memindai basis data atau
jaringan milik organisasi tanpa izin tertulis.
