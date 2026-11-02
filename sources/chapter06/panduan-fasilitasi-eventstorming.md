<!-- Panduan fasilitasi lokakarya EventStorming Bab 06. Dibaca fasilitator sebelum lokakarya dan dipakai sebagai daftar periksa selama sesi. -->

# Panduan Fasilitasi Lokakarya EventStorming

Panduan ini dipakai pada Aktivitas Bab 06, "Lokakarya EventStorming dan Context
Map". Formatnya *Big Picture* yang dipersempit pada satu alur layanan pasien,
misalnya dari pendaftaran rawat jalan sampai klaim BPJS Kesehatan. Waktu total
sekitar 240 menit, dibagi dua sesi masing-masing 120 menit.

## 1. Peran dalam tim

| Peran | Diisi oleh | Tugas utama |
| :-- | :-- | :-- |
| Pakar domain | Anggota berlatar kesehatan, manajemen, atau keuangan; sebaiknya ditambah satu atau dua narasumber dari organisasi | Menulis *domain event*, bercerita tentang alur nyata, mengoreksi urutan |
| Fasilitator | Anggota berlatar teknis | Menjaga aturan main, mengajukan pertanyaan, tidak memihak, memastikan setiap orang ikut menempel |
| Pencatat istilah | Anggota berlatar teknis kedua, atau anggota yang teliti | Memegang glosarium, mencatat istilah yang diperdebatkan sebagai *hot spot* |
| Penjaga waktu dan perangkum | Satu anggota mana pun | Mengingatkan batas waktu tiap langkah, merangkum hasil di akhir sesi |

## 2. Warna catatan tempel

| Elemen | Warna | Bentuk tulisan | Contoh |
| :-- | :-- | :-- | :-- |
| *Domain event* | Oranye | Kata kerja bentuk lampau | Pasien terdaftar |
| *Command* | Biru | Kata kerja perintah | Daftarkan pasien |
| Aktor | Kuning, kecil | Peran orang, bukan nama orang | Petugas loket |
| Sistem eksternal | Merah muda, lebar | Nama sistem | Layanan web BPJS Kesehatan |
| *Policy* | Ungu muda | "Setiap kali ..., maka ..." | Setiap kali hasil kritis tervalidasi, dokter diberi tahu |
| Informasi | Hijau | Informasi untuk mengambil keputusan | Daftar antrean poliklinik |
| *Hot spot* | Merah muda terang | Pertanyaan, masalah, atau perselisihan | Siapa menutup kunjungan bila pasien pulang sebelum bayar? |

Warna mengikuti lembar ringkas DDD Crew
(<https://github.com/ddd-crew/eventstorming-glossary-cheat-sheet>). Pada papan
virtual, warna dikunci di templat agar peserta tidak memilih warna sendiri.

## 3. Agenda dua sesi

| Sesi | Menit | Langkah | Hasil |
| :-- | --: | :-- | :-- |
| 1 | 10 | Pembukaan: tujuan, alur yang dibahas, aturan main, uji alat | Semua peserta bisa menempel catatan |
| 1 | 20 | Eksplorasi bebas: setiap orang menulis *domain event* tanpa diskusi | 40 sampai 80 catatan oranye |
| 1 | 40 | Menegakkan urutan waktu, membuang duplikat, menandai *pivotal event* | Satu garis waktu yang disepakati |
| 1 | 30 | Membaca alur dari kiri ke kanan, menandai *hot spot* | Daftar *hot spot* |
| 1 | 20 | Rangkuman dan ekspor papan | Tangkapan papan sesi 1 |
| 2 | 10 | Pengingat hasil sesi 1 | Peserta kembali ke konteks |
| 2 | 40 | Menambah *command*, aktor, sistem eksternal, dan *policy* | Pemicu setiap *event* jelas |
| 2 | 40 | Mengelompokkan *event* menjadi kandidat *bounded context* | Lima sampai delapan kelompok bernama |
| 2 | 30 | Menggambar *context map* awal dengan `templat-context-map.drawio` | *Context map* kondisi saat ini |

## 4. Aturan main

1. Satu catatan, satu kejadian. Kalimat pendek, bentuk lampau.
2. Tidak ada jawaban salah pada eksplorasi bebas. Urutan dirapikan belakangan.
3. Perdebatan yang belum selesai dalam dua menit ditulis sebagai *hot spot*,
   lalu ditinggalkan.
4. Istilah yang dipakai berbeda oleh dua orang langsung masuk glosarium.
5. Nama orang dan data pasien tidak boleh ditulis di papan.

## 5. Pertanyaan pemandu fasilitator

- "Apa yang terjadi tepat sebelum ini? Apa yang terjadi sesudahnya?"
- "Siapa yang memutuskan langkah ini, dan informasi apa yang dia butuhkan?"
- "Di titik mana pekerjaan berpindah tangan ke bagian lain?"
- "Kata ini artinya sama untuk semua yang hadir?"
- "Bila langkah ini gagal, apa yang terjadi pada pasien?"

## 6. Petunjuk batas *bounded context*

- *Pivotal event*: kejadian yang menandai pergantian tahap, misalnya
  "Kunjungan ditutup".
- Pergantian aktor atau bagian yang bertanggung jawab.
- Pergantian bahasa: istilah yang sama mulai bermakna lain.
- Pergantian ritme: bagian yang bekerja per detik dan bagian yang bekerja per
  bulan.

## 7. Daftar periksa lokakarya daring

- [ ] Papan virtual disiapkan dengan warna terkunci dan garis waktu kosong.
- [ ] Setiap peserta sudah mencoba menempel catatan sebelum sesi 1.
- [ ] Kamera menyala; giliran bicara diatur fasilitator.
- [ ] Glosarium terbuka di sisi papan dan dipegang pencatat istilah.
- [ ] Papan diekspor sebagai gambar dan PDF di akhir setiap sesi.
- [ ] Izin organisasi tercatat; data sudah dianonimkan.
