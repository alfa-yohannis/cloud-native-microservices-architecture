# Sumber Bab 10

Berkas pendukung Bab 10, Data dalam Microservices: Saga dan Outbox. Seluruh
angka dan data di dalamnya rekaan untuk kasus fiktif Medikara Health. Berkas
dipakai pada Aktivitas "Peta Kepemilikan Data dan Rancangan Saga" dan pada
Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-peta-kepemilikan-data.xlsx` | Templat peta kepemilikan data. Lembar "Contoh Medikara" berisi isi tabel peta kepemilikan di naskah; lembar "Isian Tim" dipakai untuk proses capstone tim. Kolomnya: entitas, atribut utama, layanan pemilik, layanan pembaca, cara memperoleh, sensitivitas, dan catatan. |
| `templat-rancangan-saga.md` | Templat rancangan saga: identitas saga, langkah dan kompensasi, skenario gagal, serta daftar periksa. Bagian A berisi contoh saga pendaftaran pasien rujukan; bagian B adalah isian tim. Dipakai juga pada Latihan 2. |
| `contoh-outbox-postgresql/skema-outbox.sql` | Pendalaman teknis (opsional): tabel `jadwal_dokter` dan `outbox`, indeks parsial, serta satu transaksi lokal yang mengunci slot dan mencatat *event* `JadwalDikunci` sekaligus. |
| `contoh-outbox-postgresql/penerbit-outbox.py` | Pendalaman teknis (opsional): penerbit *outbox* dengan cara *polling publisher*. *Event* ditulis ke berkas `event-terbit.jsonl` sebagai pengganti *broker*. |

Cara menjalankan contoh *outbox* (hanya pada PostgreSQL 13 atau lebih baru milik
sendiri):

```bash
cd sources/chapter10/contoh-outbox-postgresql
createdb medikara
psql -d medikara -f skema-outbox.sql
pip install "psycopg[binary]"
python penerbit-outbox.py
```

Alamat basis data dapat diganti lewat variabel lingkungan `ALAMAT_BASIS_DATA`,
misalnya `postgresql://postgres:sandi@localhost:5432/medikara`. Penerbit
berjalan terus sampai dihentikan dengan Ctrl+C. Untuk melihat jaminan
*at-least-once*, hentikan penerbit secara paksa tepat setelah satu *event*
ditulis, lalu jalankan lagi: *event* dengan `id_event` yang sama muncul dua kali.
