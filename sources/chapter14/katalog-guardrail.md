<!-- Katalog guardrail untuk Aktivitas dan Latihan 2 Bab 14. Salin berkas ini, sesuaikan tujuh contoh Medikara dengan organisasi tim, lalu isi bagian "Isian Tim". Seluruh contoh rekaan. -->

# Katalog Guardrail Tata Kelola Cloud

Tulis setiap *guardrail* dalam bahasa biasa lebih dulu, karena direksi dan auditor harus dapat
membacanya. Terjemahan ke kode kebijakan menyusul. Tim memilih lima sampai tujuh *guardrail* yang
menutup biaya, keamanan, dan lokasi data.

## Contoh Medikara Health

| No. | Rumusan bahasa biasa | Kategori | Jenis kendali | Risiko yang dicegah | Bukti kepatuhan | Pemilik | Jalur pengecualian |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| G1 | Data rekam medis dan data pribadi spesifik hanya disimpan di *region* yang berlokasi di Indonesia, termasuk cadangannya | Lokasi data | Proaktif dan preventif | Pelanggaran Permenkes 24/2022 dan UU PDP | Hasil pemeriksaan *pipeline*; daftar sumber daya per *region* | Wakil keamanan | Hanya untuk data yang sudah dianonimkan, disetujui wakil keamanan dan petugas pelindungan data, paling lama 6 bulan |
| G2 | Penyimpanan data pasien dienkripsi dengan kunci yang dikelola Medikara | Keamanan | Proaktif dan detektif | Data terbaca pihak yang tidak berhak | Laporan pemindaian enkripsi per akun | Wakil keamanan | Tidak ada untuk produksi; lingkungan uji dengan data rekaan boleh memakai kunci bawaan |
| G3 | Setiap sumber daya punya tag pemilik, layanan, lingkungan, pusat biaya, dan kelas data | Biaya | Proaktif | Tagihan tidak dapat dialokasikan; kelas data tidak diketahui | Porsi biaya tak teralokasi, sasaran di bawah 5 persen | Wakil keuangan | Sumber daya bawaan penyedia yang tidak mendukung tag dicatat dalam daftar |
| G4 | Tidak ada penyimpanan data pasien yang dapat diakses publik | Keamanan | Preventif dan detektif | Kebocoran data | Laporan pemindaian akses publik | Wakil keamanan | Tidak ada |
| G5 | Akses manusia memakai identitas perorangan dan autentikasi dua faktor; tidak ada akun bersama vendor | Keamanan | Preventif dan detektif | Temuan audit kontrol akses yang lemah | Daftar akun dan status autentikasi | Wakil keamanan | Akun darurat disegel, setiap pemakaian dilaporkan dalam 24 jam |
| G6 | Log audit dikirim ke akun log terpusat dan tidak dapat dihapus selama 1 tahun | Keamanan | Preventif | Jejak insiden hilang | Uji hapus berkala yang ditolak sistem | Wakil operasi | Tidak ada |
| G7 | Setiap akun punya anggaran bulanan dengan ambang peringatan 50, 80, dan 100 persen | Biaya | Proaktif dan detektif | Tagihan melonjak tanpa diketahui | Daftar anggaran per akun; catatan peringatan | Wakil keuangan | Tidak ada |

## Isian Tim

| No. | Rumusan bahasa biasa | Kategori | Jenis kendali | Risiko yang dicegah | Bukti kepatuhan | Pemilik | Jalur pengecualian |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... | ... | ... | ... |

## Daftar Periksa

- [ ] Biaya, keamanan, dan lokasi data masing-masing punya paling sedikit satu *guardrail*.
- [ ] Setiap rumusan dapat dibaca anggota non-teknis tanpa penjelasan tambahan.
- [ ] Setiap *guardrail* punya bukti kepatuhan yang dapat ditunjukkan kepada auditor.
- [ ] Setiap *guardrail* punya pemilik bernama jabatan, bukan nama tim umum.
- [ ] Jalur pengecualian menyebut penyetuju dan masa berlaku, atau ditulis "tidak ada" dengan alasan.
- [ ] Aturan lokasi data dicek ulang pada teks resmi di JDIH sebelum dikutip.
- [ ] Data organisasi nyata dipakai seizin organisasi dan dianonimkan.
