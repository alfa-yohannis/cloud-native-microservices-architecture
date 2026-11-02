# Berkas Pendukung Bab 09: Komunikasi Antarlayanan dan Event-Driven Architecture

Berkas di folder ini mendukung Aktivitas "Peta Interaksi Layanan dan Katalog Event", Latihan, dan Pendalaman Teknis Bab 09. Seluruh data bersifat rekaan dan memakai kasus fiktif Medikara Health. Data pribadi pasien atau karyawan tidak boleh dimasukkan ke templat.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-peta-interaksi.csv` | Templat peta interaksi layanan: langkah bisnis, layanan pengirim dan penerima, pola komunikasi (sinkron atau asinkron), alasan, dan akibat bila penerima mati. Tiga baris pertama berisi contoh alur janji temu Medikara+. |
| `templat-katalog-event.csv` | Templat katalog *event*: nama, pemilik, pemicu bisnis, pola *event*, isi data, pelanggan, kandungan data pribadi, dan versi. Berisi contoh `JanjiTemuDibuat`, `HasilLabTersedia`, dan `TagihanTerbit`. |
| `asyncapi-janji-temu.yaml` | Contoh satu baris katalog *event* yang ditulis dalam AsyncAPI 3.0.0, dengan amplop pesan CloudEvents 1.0. Dipakai sebagai pola bagi tim yang ingin menuliskan katalognya dalam format mesin. |
| `contoh-broker-lokal/docker-compose.yml` | Menjalankan RabbitMQ beserta konsol pengelolaannya di komputer sendiri untuk Pendalaman Teknis. |
| `contoh-broker-lokal/kirim_terima_event.py` | Skrip Python yang mengirim *event* `JanjiTemuDibuat` dua kali untuk meniru pengiriman *at-least-once*, lalu menerimanya dengan *consumer* yang idempoten. |

## Cara memakai contoh broker lokal

1. Pasang Docker dan Python 3, lalu masuk ke folder `contoh-broker-lokal`.
2. Jalankan `docker compose up -d`, kemudian `pip install pika`. Tunggu sekitar 10 detik sampai broker siap. Galat `StreamLostError` pada langkah berikutnya berarti broker belum siap, sehingga perintahnya cukup diulang.
3. Jalankan `python kirim_terima_event.py kirim`. Konsol `http://localhost:15672` (pengguna dan sandi `guest`) memperlihatkan dua pesan di antrean `notifikasi.janji-temu-dibuat`.
4. Jalankan `python kirim_terima_event.py terima`. Pesan pertama diproses, pesan kedua dilewati karena id-nya sudah tercatat.
5. Hentikan broker dengan `docker compose down`.

Broker ini hanya untuk komputer sendiri. Port 5672 dan 15672 tidak boleh dibuka ke jaringan publik, dan pengujian tidak boleh diarahkan ke broker milik organisasi lain tanpa izin tertulis.
