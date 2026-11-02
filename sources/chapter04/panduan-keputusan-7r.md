<!-- Panduan memberi usulan 7R per aplikasi untuk Aktivitas dan Latihan Bab 04. Dibaca berdampingan dengan templat-inventaris-aplikasi.xlsx. -->

# Panduan Keputusan 7R

Panduan ini dipakai pada Aktivitas "Penilaian Kesiapan dan Portofolio 7R" dan
pada Latihan 1 sampai 3 Bab 04. Definisi dan kasus pemakaian setiap strategi
mengikuti AWS Prescriptive Guidance, *About the migration strategies*
(<https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html>).
Contoh Medikara Health seluruhnya rekaan.

## 1. Urutan pertanyaan

Pertanyaan diajukan berurutan. Jawaban pertama yang cocok menentukan usulan awal.
Urutan ini sama dengan diagram alur keputusan 7R di naskah bab
(`figures/ch04-pohon-7r.tex`).

| No | Pertanyaan | Bila jawabannya | Usulan |
| --- | --- | --- | --- |
| 1 | Apakah aplikasi masih bernilai bagi bisnis? | Tidak | Retire |
| 2 | Apakah aplikasi harus tetap di tempat untuk sementara waktu? | Ya | Retain |
| 3 | Apakah ada produk atau SaaS pengganti yang layak? | Ya | Repurchase |
| 4 | Apakah ada tuntutan bisnis kuat dan strategi lain tidak memadai? | Ya | Refactor |
| 5 | Apakah perubahan kecil membuat aplikasi jauh lebih efisien? | Ya | Replatform |
| 6 | Apakah platform virtualisasinya dapat dipindah utuh? | Ya | Relocate |
| 7 | Bila semua jawaban di atas tidak cocok | | Rehost |

## 2. Bukti minimal untuk setiap usulan

| Usulan | Bukti yang diminta | Tanda bahaya |
| --- | --- | --- |
| Retire | Data pemakaian 90 hari; pemakaian prosesor dan memori di bawah 5 persen atau tanpa koneksi masuk; rencana arsip data | Pemilik bisnis tidak dapat ditemukan, tetapi aturan retensi data masih berlaku |
| Retain | Alasan tertulis: aturan lokasi data, perangkat khusus, dependensi yang harus pindah lebih dulu, investasi baru, atau menunggu versi SaaS; tanggal tinjau ulang | Retain tanpa tanggal tinjau ulang menjadi "tidak pernah" |
| Rehost | Sistem operasi didukung penyedia; tidak ada lisensi yang terikat perangkat keras | Masalah aplikasi ikut pindah apa adanya |
| Relocate | Platform virtualisasi yang sama tersedia di *cloud*, atau perpindahan antarakun | Biaya lisensi platform tetap ditanggung |
| Repurchase | Kecocokan fitur, keamanan, dan kepatuhan produk pengganti; rencana pindah data dan pelatihan | Kustomisasi lama dipaksakan ke produk baru |
| Replatform | Daftar perubahan yang terbatas dan jelas, misalnya basis data ke layanan terkelola | Daftar perubahan terus bertambah sampai menjadi Refactor |
| Refactor | Tuntutan bisnis yang terukur (skala, kecepatan rilis); tim dan anggaran tersedia | Dipilih karena teknologinya menarik, bukan karena kebutuhan bisnis |

## 3. Aturan saat usulan diperdebatkan

1. Tulis dua pilihan yang bersaing, bukan satu pilihan dengan catatan "mungkin".
2. Bandingkan keduanya dengan kriteria berbobot yang disepakati tim sebelum skor
   diisi (lihat bagian 4).
3. Catat asumsi yang paling memengaruhi hasil, lalu tentukan siapa yang
   memastikan asumsi itu dan kapan.
4. Bila selisih skor kurang dari 0,3, keputusan diserahkan ke forum tata kelola
   dengan kedua pilihan beserta alasannya.

## 4. Lembar pembanding dua pilihan (Latihan 2)

Bobot di bawah ini contoh. Tim boleh mengubahnya, asalkan alasan perubahan ditulis
sebelum skor diisi. Skor 1 sampai 5, makin besar makin baik.

### Contoh terisi: aplikasi apotek Medikara Health

| Kriteria | Bobot | Repurchase | Rehost |
| --- | --- | --- | --- |
| Kesesuaian dengan strategi "Satu Pasien, Satu Rekam Medis" | 30% | 5 | 2 |
| Waktu sampai manfaat terasa | 20% | 4 | 5 |
| Biaya lima tahun | 20% | 4 | 3 |
| Risiko layanan saat peralihan | 20% | 3 | 4 |
| Beban perubahan bagi pengguna | 10% | 2 | 5 |
| **Skor berbobot** | 100% | **3,9** | **3,5** |

### Lembar isian: SIMRS

| Kriteria | Bobot | Pilihan usulan: ... | Pilihan alternatif: ... |
| --- | --- | --- | --- |
| ... | ... | ... | ... |
| ... | ... | ... | ... |
| ... | ... | ... | ... |
| ... | ... | ... | ... |
| ... | ... | ... | ... |
| **Skor berbobot** | 100% | ... | ... |

## 5. Etika

Data organisasi nyata dipakai hanya seizin organisasi dan dianonimkan. Nama
aplikasi boleh disamarkan. Data pribadi pasien atau karyawan tidak boleh masuk ke
inventaris, termasuk dalam tangkapan layar.
