<!-- Daftar pertanyaan dan bukti per faktor untuk Aktivitas Bab 05. Pakai: bawa ke wawancara tim TI atau vendor, lalu catat jawabannya di kartu skor. -->

# Pertanyaan dan Bukti per Faktor Twelve-Factor App

Daftar ini membantu tim menilai satu aplikasi tanpa harus membaca kodenya.
Pertanyaan ditulis dalam bahasa sehari-hari agar dapat diajukan oleh anggota
berlatar non-teknis. Anggota berlatar teknis memeriksa apakah jawabannya didukung
bukti. Bunyi faktor mengacu pada <https://12factor.net/>; catat tanggal aksesnya
di kartu skor karena teksnya kini dikelola komunitas dan dapat berubah.

| Faktor | Pertanyaan untuk tim TI atau vendor | Bukti yang dicari | Tanda skor 3 | Tanda skor 0 |
| --- | --- | --- | --- | --- |
| I Codebase | Berapa salinan kode aplikasi ini yang dirawat terpisah? | Daftar repositori, cara perbaikan disebarkan | Satu repositori untuk semua lokasi | Setiap lokasi punya salinan sendiri |
| II Dependencies | Bagaimana server baru disiapkan untuk aplikasi ini? | Berkas daftar pustaka dan versinya | Semua pustaka tertulis dan terpasang otomatis | Pustaka dipasang manual dari ingatan |
| III Config | Bila alamat layanan luar berubah, apa yang harus diubah? | Letak kata sandi dan alamat (tanpa menyalin nilainya) | Cukup ubah lingkungan, tanpa rilis ulang | Kode harus diubah dan dibangun ulang |
| IV Backing services | Bila basis data dipindah ke server lain, berapa lama pekerjaannya? | Cara aplikasi menyebut basis data dan layanan luar | Cukup ganti alamat di konfigurasi | Alamat tertanam di banyak tempat |
| V Build, release, run | Bagaimana versi baru sampai ke produksi, dan dapatkah kembali ke versi lama? | Prosedur rilis, catatan nomor rilis | Rilis bernomor, kembali ke versi lama dalam menit | Kode diubah langsung di server |
| VI Processes | Bila satu server mati, apakah pengguna harus masuk ulang? | Letak penyimpanan sesi | Sesi di penyimpanan bersama | Sesi di memori satu server |
| VII Port binding | Apakah aplikasi butuh server web yang dipasang terpisah agar dapat berjalan? | Cara aplikasi dinyalakan | Aplikasi melayani sendiri lewat port | Bergantung pada server web terpasang |
| VIII Concurrency | Bagaimana kapasitas ditambah saat ramai? | Catatan penanganan lonjakan terakhir | Menambah proses yang sama | Hanya mengganti server menjadi lebih besar |
| IX Disposability | Berapa lama satu server baru siap melayani? Apa yang terjadi saat dimatikan? | Waktu mulai, perilaku saat berhenti | Menyala dalam detik, berhenti rapi | Menyala belasan menit, data rusak saat mati |
| X Dev/prod parity | Seberapa mirip lingkungan uji dengan produksi? | Versi basis data dan sistem operasi tiap lingkungan | Sama, dan kode sampai ke produksi dalam jam | Berbeda, dan kode sampai dalam bulan |
| XI Logs | Bila terjadi gangguan, di mana jejaknya dicari dan berapa lama disimpan? | Letak log, lama penyimpanan, format | Terkumpul di satu tempat dan dapat dicari | Berkas lokal per server, umur pendek |
| XII Admin processes | Bagaimana perbaikan data atau migrasi basis data dijalankan? | Prosedur dan catatan tugas administratif | Skrip tersimpan bersama kode, dijalankan di lingkungan yang sama | Dijalankan manual dari laptop tanpa catatan |

## Catatan etika

- Jangan menyalin kata sandi, kunci akses, alamat internal, atau data pribadi
  pasien dan karyawan. Tulis keberadaannya saja, misalnya "kata sandi basis data
  tertulis di berkas kode".
- Wawancara hanya dengan narasumber yang bersedia, setelah tujuan dan pemakaian
  catatannya dijelaskan.
