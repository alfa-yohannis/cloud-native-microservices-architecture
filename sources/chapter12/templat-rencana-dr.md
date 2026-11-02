<!-- Kegunaan: templat rencana resiliensi dan DR (Disaster Recovery) untuk Aktivitas Bab 12. Cara pakai: salin berkas ini menjadi rencana-dr-nama-layanan.md, isi setiap bagian dengan angka dari templat-analisis-dampak-bisnis.xlsx, lalu lampirkan pada berkas tonggak C4. -->

# Templat Rencana Resiliensi dan Disaster Recovery

Satu rencana mencakup satu layanan kritis atau satu kelompok layanan yang selalu
dipulihkan bersama. Rencana ditulis agar dapat dibaca pemilik bisnis dan
dijalankan petugas jaga pada pukul tiga dini hari tanpa penulisnya.

## 1. Identitas

| Butir | Isi |
| :-- | :-- |
| Nama layanan | (misalnya rekam medis elektronik) |
| Pemilik bisnis | (jabatan, bukan nama orang) |
| Pemilik teknis | (tim yang menjaga layanan) |
| Versi rencana dan tanggal | (misalnya 1.0, 14 November 2026) |
| Tanggal uji pemulihan terakhir | (belum pernah / tanggal) |

## 2. Hasil analisis dampak bisnis

Salin ringkasan dari lembar Isian Tim pada `templat-analisis-dampak-bisnis.xlsx`.

| Butir | Isi |
| :-- | :-- |
| Dampak bila berhenti | ... |
| Kerugian finansial per jam | Rp... juta |
| Dampak keselamatan pasien | rendah / sedang / tinggi, beserta alasannya |
| Kewajiban regulasi | ... |
| Waktu henti maksimum yang dapat ditoleransi | ... jam |
| RTO (*Recovery Time Objective*) | ... jam |
| RPO (*Recovery Point Objective*) | ... menit |

Periksa: RTO lebih pendek dari waktu henti maksimum yang dapat ditoleransi.

## 3. Pola resiliensi

| Ketergantungan | *Timeout* | *Retry* dan *backoff* | *Circuit breaker* | *Bulkhead* | *Graceful degradation* |
| :-- | :-- | :-- | :-- | :-- | :-- |
| (misalnya layanan kepesertaan BPJS Kesehatan) | ... detik | ... kali, jeda ... | ambang ..., terbuka ... detik | kolam koneksi terpisah ... | (perilaku yang terasa oleh pengguna) |
| ... | ... | ... | ... | ... | ... |

Pastikan *retry* hanya dilakukan di satu lapis, dan hanya untuk operasi yang
aman diulang.

## 4. Arsitektur DR

| Butir | Isi |
| :-- | :-- |
| Strategi | *backup and restore* / *pilot light* / *warm standby* / *multi-site active-active* |
| Lokasi utama | (misalnya *region* Jakarta, tiga AZ) |
| Lokasi kedua | (lokasi dan alasan pemilihannya, termasuk kendala lokasi data dari Bab 2) |
| Cara data disalin | replikasi sinkron / asinkron / cadangan berkala, dengan jadwalnya |
| Cadangan terpisah yang tidak dapat diubah | lokasi, akun, masa kunci, siapa yang dapat menghapus |
| Perkiraan biaya DR per tahun | Rp... juta, beserta asumsi |

## 5. Kriteria deklarasi bencana

Tuliskan kondisi terukur yang membuat pemulihan ke lokasi kedua dimulai, dan
jabatan yang berwenang memutuskannya. Contoh: "layanan tidak tersedia lebih
dari 20 menit dan penyedia belum memberi perkiraan pulih".

## 6. Peran dan jalur komunikasi

| Peran | Jabatan | Cadangan bila berhalangan | Cara dihubungi |
| :-- | :-- | :-- | :-- |
| Pemimpin pemulihan | ... | ... | ... |
| Penghubung bisnis (IGD, rawat jalan, keuangan) | ... | ... | ... |
| Penghubung komunikasi publik | ... | ... | ... |
| Penghubung penyedia dan mitra | ... | ... | ... |

## 7. Urutan pemulihan

1. ...
2. ...
3. ...

Catat ketergantungan: layanan apa yang harus pulih lebih dahulu (misalnya
identitas dan direktori pengguna sebelum aplikasi klinis).

## 8. Prosedur pindah (*failover*) dan kembali (*failback*)

Tuliskan langkah bernomor, perkiraan waktu setiap langkah, dan cara memeriksa
bahwa langkah berhasil. Jumlah perkiraan waktu harus lebih pendek dari RTO.

## 9. Jadwal uji pemulihan

| Jenis uji | Cakupan | Frekuensi | Tanggal berikutnya | Penanggung jawab |
| :-- | :-- | :-- | :-- | :-- |
| Pemulihan cadangan ke lingkungan terpisah | ... | (misalnya bulanan) | ... | ... |
| Latihan meja (*tabletop*) | ... | (misalnya per semester) | ... | ... |
| *Game day* dengan pemindahan nyata | ... | (misalnya tahunan) | ... | ... |

## 10. Risiko dan asumsi

- ...
- ...

## Daftar periksa sebelum diajukan

- [ ] RTO dan RPO berasal dari analisis dampak bisnis, bukan dari kemampuan teknologi yang ada.
- [ ] RTO lebih pendek dari waktu henti maksimum yang dapat ditoleransi.
- [ ] Ada salinan cadangan yang terpisah akun dan tidak dapat diubah selama masa kunci.
- [ ] Lokasi kedua sesuai kendala lokasi data (Bab 2).
- [ ] Prosedur dapat dijalankan oleh orang selain penulisnya.
- [ ] Ada tanggal uji pemulihan berikutnya dan penanggung jawabnya.
- [ ] Biaya DR dibandingkan dengan perkiraan kerugian, dan pemilik bisnis menyetujuinya.
