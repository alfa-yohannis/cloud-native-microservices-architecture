<!-- Kegunaan: templat ADR (Architecture Decision Record) untuk Aktivitas Bab 07. Cara pakai: salin berkas ini menjadi adr-001-judul-singkat.md, isi setiap bagian, lalu simpan di folder dokumen capstone tim. -->

# Templat Architecture Decision Record

Satu berkas berisi satu keputusan. Nomor ADR berurutan dan tidak dipakai ulang.
ADR yang sudah diterima tidak diedit isinya. Bila keputusan berubah, tim menulis
ADR baru dan mengubah status ADR lama menjadi "Digantikan oleh ADR-00N".


## ADR-00N: (judul singkat berupa keputusan, misalnya "SIMRS terpadu memakai gaya *modular monolith*")

**Status.** Diusulkan / Diterima / Ditolak / Usang / Digantikan oleh ADR-00N

**Tanggal dan pengambil keputusan.** (tanggal; nama jabatan, bukan nama orang,
misalnya "komite arsitektur: direktur TI, direktur pelayanan, direktur keuangan")

### Konteks

Tuliskan fakta yang memaksa keputusan ini diambil sekarang. Pakai angka dari
lembar diagnosis.

- Masalah bisnis yang ingin diselesaikan:
- Fakta dari diagnosis (perubahan bersama, gangguan, tim pengelola):
- Kendala (anggaran, kapasitas tim, regulasi, kontrak vendor):
- Keputusan lain yang terkait (nomor ADR lain, bila ada):

### Opsi yang Ditimbang

Minimal tiga opsi. Opsi "tidak berubah" boleh menjadi salah satunya.

| Opsi | Uraian singkat | Kelebihan | Kekurangan |
| :-- | :-- | :-- | :-- |
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Keputusan

Opsi yang dipilih dan dua atau tiga alasan utamanya. Tuliskan juga alasan
setiap opsi lain ditolak dalam satu kalimat.

### Konsekuensi

| Jenis | Konsekuensi | Cara mengelola |
| :-- | :-- | :-- |
| Baik | | |
| Buruk | | |
| Risiko | | |

### Syarat Peninjauan Ulang

Kondisi terukur yang membuat keputusan ini perlu ditinjau, misalnya "waktu
tunggu rilis modul klaim lebih dari dua minggu selama tiga bulan berturut-turut".


## Daftar Periksa Sebelum ADR Diajukan

- [ ] Judul berupa keputusan, bukan topik ("Memakai X", bukan "Tentang X").
- [ ] Konteks memuat angka dari diagnosis, bukan pendapat.
- [ ] Ada minimal tiga opsi, termasuk yang ditolak dan alasannya.
- [ ] Konsekuensi buruk ditulis sejujur konsekuensi baik.
- [ ] Bahasa dapat dipahami anggota manajemen dan auditor tanpa penjelasan lisan.
- [ ] Syarat peninjauan ulang dapat diukur.
- [ ] Tidak ada data pribadi pasien atau karyawan.
