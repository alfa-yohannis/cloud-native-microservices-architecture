<!-- Kegunaan: contoh skenario game day dan templat kosongnya untuk Aktivitas Bab 12. Cara pakai: baca contoh Medikara, lalu salin bagian "Templat skenario tim" dan isi untuk layanan kritis tim. Seluruh angka pada contoh adalah rekaan. -->

# Skenario Game Day: Region Utama Tidak Tersedia Selama Empat Jam

*Game day* adalah latihan terjadwal untuk menguji rencana pemulihan bersama tim
teknis dan bisnis. Contoh ini berbentuk latihan meja (*tabletop*): peserta
duduk bersama, fasilitator membacakan kejadian satu per satu, dan peserta
menjawab apa yang akan dilakukan. Tidak ada sistem produksi yang disentuh.
Latihan dengan pemindahan nyata baru dilakukan setelah latihan meja berjalan
baik dan syarat aman pada bagian akhir terpenuhi.

## Contoh Medikara Health

**Hipotesis.** Bila *region* utama tidak tersedia, rekam medis elektronik pulih
di lokasi kedua dalam 1 jam dengan data hilang paling banyak 5 menit. Medikara+
pulih dalam 4 jam. ERP keuangan boleh menunggu sampai 24 jam.

**Waktu latihan.** Sabtu, 09.00 sampai 12.00, di ruang rapat kantor pusat.
Latihan meja tidak mengganggu layanan, sehingga tidak perlu jam sepi.

**Peserta.**

| Peran dalam latihan | Jabatan |
| :-- | :-- |
| Fasilitator | Anggota tim capstone yang tidak ikut menjawab |
| Pemimpin pemulihan | Kepala operasi TI |
| Penghubung klinis | Kepala IGD dan kepala instalasi rekam medis RS Jakarta |
| Penghubung bisnis | Perwakilan keuangan dan layanan pasien |
| Penghubung komunikasi | Humas |
| Pencatat waktu | Satu anggota tim, mencatat jam setiap keputusan |

**Urutan kejadian (diberikan fasilitator satu per satu).**

| Menit | Kejadian yang dibacakan | Pertanyaan untuk peserta |
| :-- | :-- | :-- |
| 0 | Pukul 07.40 pemantauan mencatat rekam medis elektronik, Medikara+, dan layanan integrasi tidak dapat diakses. Halaman status penyedia menyebut gangguan jaringan di *region* utama. | Siapa yang pertama dihubungi? Lewat jalur apa? |
| 10 | Penyedia belum memberi perkiraan pulih. IGD RS Jakarta mulai memakai formulir kertas. | Apakah kriteria deklarasi bencana sudah terpenuhi? Siapa yang memutuskan? |
| 20 | Pemimpin pemulihan menyatakan bencana. | Langkah pemindahan pertama apa? Berapa lama perkiraannya? |
| 35 | Basis data rekam medis di lokasi kedua aktif. Replikasi terakhir tercatat pukul 07.36. | Berapa data yang hilang? Masih dalam RPO 5 menit? Siapa yang memasukkan ulang entri pukul 07.36 sampai 07.40? |
| 50 | Aplikasi rekam medis di lokasi kedua menyala, tetapi petugas tidak dapat masuk karena layanan identitas hanya ada di *region* utama. | Ketergantungan apa yang terlewat di rencana? Apa jalan keluarnya sekarang? |
| 80 | Petugas dapat masuk. Rekam medis pulih. | Apakah RTO 1 jam terpenuhi? Apa yang dicatat untuk perbaikan? |
| 120 | Pasien mengeluh di media sosial karena Medikara+ belum dapat dipakai. | Pesan apa yang disampaikan humas? Kapan Medikara+ dijadwalkan pulih? |
| 240 | *Region* utama kembali normal. | Kapan dan bagaimana kembali ke *region* utama (*failback*)? Siapa yang menyetujui? |

**Kriteria berhasil.**

1. Keputusan deklarasi bencana diambil paling lambat menit ke-20 oleh jabatan yang tertulis di rencana.
2. Perkiraan waktu pemulihan rekam medis, dijumlahkan dari langkah-langkahnya, kurang dari 1 jam.
3. Setiap ketergantungan yang terlewat dicatat bersama pemilik perbaikannya.
4. Pesan kepada pasien dan mitra disiapkan sebelum menit ke-30.

**Catatan contoh hasil.** Pada contoh ini rekam medis baru pulih pada menit
ke-80, sehingga RTO 1 jam tidak terpenuhi. Penyebabnya layanan identitas yang
tidak ikut disiapkan di lokasi kedua. Perbaikannya dicatat sebagai butir
tindak lanjut dengan pemilik dan tenggat, lalu diuji ulang pada latihan
berikutnya.

## Templat skenario tim

**Hipotesis.** Bila ..., layanan ... pulih dalam ... dengan data hilang paling banyak ....

**Waktu dan bentuk latihan.** (latihan meja / pemindahan nyata di lingkungan uji / pemindahan nyata di produksi)

**Peserta.**

| Peran dalam latihan | Jabatan |
| :-- | :-- |
| Fasilitator | ... |
| Pemimpin pemulihan | ... |
| Penghubung bisnis | ... |
| Pencatat waktu | ... |

**Urutan kejadian.**

| Menit | Kejadian yang dibacakan | Pertanyaan untuk peserta |
| :-- | :-- | :-- |
| 0 | ... | ... |
| ... | ... | ... |

**Kriteria berhasil.**

1. ...
2. ...

**Lembar evaluasi sesudah latihan.**

| Temuan | Dampak bila terjadi sungguhan | Perbaikan | Pemilik | Tenggat |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |

## Syarat aman sebelum pemindahan nyata

- Hipotesis dan keadaan normal ditulis dengan ukuran yang dapat dipantau, misalnya SLO dari Bab 11.
- Cakupan dampak dibatasi: satu layanan, satu rumah sakit, atau sebagian kecil lalu lintas.
- Kriteria berhenti tertulis dan ada orang yang berwenang menghentikan latihan kapan saja.
- Izin tertulis dari pemilik sistem dan pemilik bisnis sudah diperoleh. Kegiatan ini hanya untuk sistem milik sendiri atau sistem yang sudah berizin tertulis.
- Pemantauan berjalan dan dapat dilihat seluruh peserta selama latihan.
- Cara kembali ke keadaan semula sudah diuji di lingkungan uji.
- Unit klinis, pusat panggilan, dan mitra yang mungkin terdampak sudah diberi tahu.
