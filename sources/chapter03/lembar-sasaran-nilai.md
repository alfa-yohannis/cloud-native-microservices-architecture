<!-- Kegunaan: lembar kerja Aktivitas Bab 03 untuk merumuskan metrik biaya per unit dan sasaran nilai cloud. Salin berkas ini, lalu isi bagian bertanda "...". -->

# Lembar Sasaran Nilai Cloud

Lembar ini dipakai pada Aktivitas Bab 03 dan menjadi bagian tonggak capstone
C1 (Konteks dan Strategi). Satu lembar untuk satu *workload*. Bagian A berisi
contoh dari kasus fiktif Medikara Health. Bagian B diisi tim.

Data organisasi nyata wajib seizin organisasi dan dianonimkan. Data pribadi
pasien atau karyawan tidak boleh dicantumkan.

## A. Contoh terisi: SIMRS rumah sakit Bekasi (angka rekaan)

| Unsur | Isi |
| :-- | :-- |
| *Workload* | SIMRS rumah sakit Bekasi, dari matriks kendala penempatan Bab 02 |
| Pemilik layanan | Kepala instalasi SIMRS rumah sakit Bekasi |
| TCO kondisi sekarang (5 tahun) | Rp5,9 miliar, atau Rp1,18 miliar per tahun |
| Opsi *cloud* yang dibandingkan | A: *rehost* dengan *on-demand* (Rp6,01 miliar); B: *rehost* dengan *rightsizing* dan komitmen (Rp4,75 miliar) |
| Metrik biaya per unit | Biaya infrastruktur per kunjungan pasien |
| Rumus | Biaya infrastruktur SIMRS per tahun dibagi jumlah kunjungan pasien rumah sakit Bekasi per tahun |
| Sumber data | Laporan biaya TI (keuangan) dan jumlah kunjungan dari SIMRS |
| Nilai awal (*baseline*) | Rp5.619 per kunjungan (210.000 kunjungan per tahun) |
| Sasaran nilai | Turun 15 persen menjadi paling tinggi Rp4.776 per kunjungan dalam dua tahun |
| Metrik pendamping | Ketersediaan SIMRS tidak turun di bawah tingkat sekarang; jejak karbon per kunjungan dicatat sebagai nilai awal |
| Asumsi kunci | Jumlah kunjungan stabil; harga komitmen tidak naik; lisensi dibawa ke *cloud* |
| Risiko terbesar | Komitmen dibeli sebelum *rightsizing* selesai, sehingga komitmen terlalu besar |
| Pemantau | Analis FinOps dan bagian akuntansi manajemen, ditinjau setiap triwulan |

## B. Isian tim

| Unsur | Isi |
| :-- | :-- |
| *Workload* | ... |
| Pemilik layanan | ... |
| TCO kondisi sekarang | ... |
| Opsi *cloud* yang dibandingkan | ... |
| Metrik biaya per unit | ... |
| Rumus | ... |
| Sumber data | ... |
| Nilai awal (*baseline*) | ... |
| Sasaran nilai | ... |
| Metrik pendamping | ... |
| Asumsi kunci | ... |
| Risiko terbesar | ... |
| Pemantau | ... |

## C. Pemeriksaan sebelum dikumpulkan

- [ ] Sasaran nilai memuat angka, arah, dan batas waktu.
- [ ] Unit dapat dipahami direksi tanpa penjelasan teknis.
- [ ] Data pembilang dan penyebut tersedia rutin, minimal bulanan.
- [ ] Setiap angka TCO punya asumsi dan sumber di `templat-tco-sederhana.xlsx`.
- [ ] Ada metrik pendamping agar penghematan tidak mengorbankan layanan.
