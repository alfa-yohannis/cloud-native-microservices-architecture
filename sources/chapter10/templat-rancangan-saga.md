<!-- Kegunaan: templat rancangan saga untuk Aktivitas dan Latihan 2 Bab 10. Salin berkas ini, isi bagian bertanda "...", lalu lampirkan ke luaran C3. -->

# Templat Rancangan Saga

Templat ini dipakai pada Aktivitas Bab 10, "Peta Kepemilikan Data dan Rancangan
Saga", dan menjadi bagian tonggak capstone C3 (Kondisi Target). Bagian A berisi
contoh terisi dari kasus fiktif Medikara Health. Bagian B adalah isian tim.
Seluruh angka pada contoh adalah rekaan.

## A. Contoh terisi: saga pendaftaran pasien rujukan

### A.1 Identitas saga

| Butir | Isi |
| :-- | :-- |
| Nama saga | Pendaftaran pasien rujukan dari klinik mitra sampai klaim terkirim |
| Pemicu | Klinik mitra mengirim rujukan lewat portal mitra |
| Selesai berhasil bila | Klaim BPJS Kesehatan berstatus terkirim |
| Selesai gagal bila | Rujukan berstatus ditolak dan klinik mitra sudah diberi tahu |
| Pola koordinasi | *Orchestration*, pengatur saga berada di Layanan Rujukan |
| Alasan pola koordinasi | Enam layanan terlibat, klinik mitra perlu melihat status, dan auditor perlu menelusuri setiap langkah |
| Volume | Sekitar 3.600 rujukan per bulan; sekitar 4 persen gagal verifikasi kepesertaan |

### A.2 Langkah dan kompensasi

| No | Layanan | Transaksi lokal | Kompensasi | Jenis | Event yang diterbitkan (lewat *outbox*) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| T1 | Rujukan | Rujukan dicatat, status MENUNGGU_VERIFIKASI | Status DITOLAK, klinik mitra menerima alasan | Dapat dikompensasi | RujukanDiterima |
| T2 | Identitas Pasien | Pasien dicocokkan dengan identitas induk | Tautan rujukan dilepas; identitas tetap | Dapat dikompensasi | PasienDicocokkan |
| T3 | Jadwal | Slot dokter spesialis dikunci | Slot dilepas, pasien dan klinik mitra diberi tahu | Dapat dikompensasi | JadwalDikunci |
| T4 | Penjaminan | Kepesertaan BPJS Kesehatan diverifikasi | Tidak ada; bila gagal, kompensasi C3, C2, C1 berjalan | Titik penentu | KepesertaanTerverifikasi |
| T5 | Tagihan | Tagihan terbit setelah kunjungan | Tidak dikompensasi; koreksi lewat tagihan baru | Dapat diulang | TagihanTerbit |
| T6 | Klaim | Klaim dikirim ke BPJS Kesehatan | Tidak dikompensasi; dikirim ulang sampai diterima | Dapat diulang | KlaimTerkirim |

### A.3 Skenario gagal

| Skenario | Langkah yang sudah selesai | Kompensasi berurutan | Pihak yang diberi tahu | Batas waktu |
| :-- | :-- | :-- | :-- | :-- |
| Slot dokter tidak tersedia (T3 gagal) | T1, T2 | Tawarkan rumah sakit lain; bila ditolak: C2, lalu C1 | Pasien, klinik mitra | 2 jam kerja |
| Layanan Klaim tidak tersedia 6 jam (T6 tertunda) | T1 sampai T5 | Tidak ada; klaim diulang otomatis | Bagian klaim bila lewat 1 hari | 1 hari kerja |

## B. Isian tim

### B.1 Identitas saga

| Butir | Isi |
| :-- | :-- |
| Nama saga | ... |
| Pemicu | ... |
| Selesai berhasil bila | ... |
| Selesai gagal bila | ... |
| Pola koordinasi | ... |
| Alasan pola koordinasi | ... |
| Volume | ... |

### B.2 Langkah dan kompensasi

| No | Layanan | Transaksi lokal | Kompensasi | Jenis | Event yang diterbitkan (lewat *outbox*) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| T1 | ... | ... | ... | ... | ... |
| T2 | ... | ... | ... | ... | ... |
| T3 | ... | ... | ... | ... | ... |
| T4 | ... | ... | ... | ... | ... |
| T5 | ... | ... | ... | ... | ... |

### B.3 Skenario gagal (minimal dua)

| Skenario | Langkah yang sudah selesai | Kompensasi berurutan | Pihak yang diberi tahu | Batas waktu |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## C. Daftar periksa sebelum diserahkan

- [ ] Setiap langkah punya tepat satu layanan pemilik, sesuai peta kepemilikan data.
- [ ] Titik penentu sudah ditandai, dan langkah sesudahnya dapat diulang.
- [ ] Kompensasi ditulis dalam bahasa bisnis dan sudah diperiksa anggota non-teknis.
- [ ] Setiap langkah yang menerbitkan *event* memakai *outbox*.
- [ ] Setiap *consumer* punya cara menolak *event* yang datang dua kali.
- [ ] Status sementara yang dilihat pasien atau mitra sudah ditulis, misalnya "menunggu verifikasi".
