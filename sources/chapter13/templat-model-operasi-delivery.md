<!-- Templat Aktivitas Bab 13: salin berkas ini, ganti baris contoh Medikara dengan data tim, lalu lampirkan ke berkas tonggak C4. -->

# Model Operasi Delivery dan Peta Jalan Platform Internal

Organisasi: ...
Anggota tim dan peran: ...
Sumber data (tiket, catatan rilis, wawancara) dan izin pemakaiannya: ...

Baris bertanda "Contoh Medikara" adalah contoh dari naskah Bab 13 (rekaan).
Hapus baris contoh setelah tim mengisi datanya sendiri.

## A. Pemetaan alur perubahan saat ini

Pilih satu perubahan kecil yang baru selesai, lalu telusuri dari permintaan
pertama sampai berjalan di produksi. Waktu proses adalah waktu kerja nyata.
Waktu tunggu adalah waktu sampai langkah berikutnya dimulai. Satuan: hari
kalender.

| No | Langkah | Pelaku | Waktu proses | Waktu tunggu sesudahnya | Jenis langkah |
| --: | :-- | :-- | --: | --: | :-- |
| 1 | Contoh Medikara: tiket diajukan dan diklasifikasi | Bagian pendaftaran, layanan bantuan | 0,5 | 4 | Kerja manual |
| 2 | Contoh Medikara: persetujuan kepala instalasi rekam medis | Kepala instalasi | 0,5 | 6 | Persetujuan |
| 3 | Contoh Medikara: persetujuan komite perubahan bulanan | Komite perubahan | 0,5 | 21 | Persetujuan |
| 4 | Contoh Medikara: antre menunggu pengembang | Tim TI RS Jakarta | 0 | 20 | Antrean |
| 5 | Contoh Medikara: pemrograman dan tinjauan kode | Pengembang | 2 | 3 | Kerja |
| 6 | Contoh Medikara: uji fungsional manual | Penguji | 1 | 28 | Uji manual |
| 7 | Contoh Medikara: uji regresi seluruh SIMRS | Enam penguji | 5 | 4 | Uji manual |
| 8 | Contoh Medikara: rilis Sabtu malam, henti layanan 4 jam | Tim TI dan vendor | 0,5 | 0 | Rilis manual |
| ... | ... | ... | ... | ... | ... |

Ringkasan (Contoh Medikara di kurung):

- Total waktu proses: ... (10 hari)
- Total waktu tunggu: ... (86 hari)
- Lead time permintaan, yaitu waktu proses ditambah waktu tunggu: ... (96 hari)
- Efisiensi alur, yaitu waktu proses dibagi lead time permintaan: ... (10,4 persen)
- Waktu sebelum pemrograman dimulai: ... (52,5 hari)
- Jumlah persetujuan, antrean, uji manual, dan rilis manual: ... (2, 1, 2, 1)

## B. Metrik DORA saat ini

Isi dari keluaran `hitung-metrik-dora.py` atau hitung manual dari catatan rilis
satu tahun.

| Metrik | Aplikasi 1 | Aplikasi 2 | Sumber data |
| :-- | :-- | :-- | :-- |
| Deployment per tahun (darurat) | ... | ... | ... |
| Lead time perubahan rata-rata | ... | ... | ... |
| Tingkat kegagalan perubahan | ... | ... | ... |
| Waktu pemulihan median | ... | ... | ... |
| Tingkat pengerjaan ulang | ... | ... | ... |
| Perubahan per rilis terjadwal | ... | ... | ... |

## C. Alur target CI/CD dan GitOps

| Tahap | Otomatis atau manual | Gerbang persetujuan | Bukti untuk auditor | Sasaran waktu |
| :-- | :-- | :-- | :-- | :-- |
| Contoh Medikara: permintaan masuk daftar kerja tim domain | Manual | Pemilik produk, mingguan | Riwayat daftar kerja | 5 hari |
| Contoh Medikara: pemrograman dan pull request | Manual | Satu peninjau kode | Komentar dan persetujuan pull request | 2 hari |
| Contoh Medikara: build, uji otomatis, pemindaian | Otomatis | Pipeline harus lolos | Log pipeline | 40 menit |
| Contoh Medikara: staging dan uji penerimaan | Otomatis dan manual | Perwakilan pengguna | Catatan uji penerimaan | 1 hari |
| Contoh Medikara: rilis canary lewat GitOps | Otomatis | Pull request ke repositori konfigurasi | Commit, persetujuan, riwayat sinkronisasi | 1 hari |
| ... | ... | ... | ... | ... |

Aturan persetujuan berbasis risiko yang diusulkan tim: ...

## D. Topologi tim target

| Tim | Tipe tim | Anggota (jumlah dan asal) | Tanggung jawab | Mode interaksi utama |
| :-- | :-- | :-- | :-- | :-- |
| Contoh Medikara: tim pendaftaran dan jadwal | Stream-aligned | 5: 3 pengembang, 2 dari unit pengguna | Pendaftaran dan jadwal dokter | X-as-a-Service dengan tim platform |
| Contoh Medikara: tim rekam medis | Stream-aligned | 5 | Rekam medis, rawat inap, radiologi | Collaboration 3 bulan dengan tim integrasi |
| Contoh Medikara: tim farmasi dan laboratorium | Stream-aligned | 5 | Farmasi dan laboratorium | X-as-a-Service dengan tim platform |
| Contoh Medikara: tim penagihan dan klaim | Stream-aligned | 5 | Penagihan, klaim BPJS, laporan | X-as-a-Service dengan tim integrasi |
| Contoh Medikara: tim Medikara+ | Stream-aligned | 5: 2 pengembang, 1 penguji, 1 perancang antarmuka, 1 pemilik produk, bersama vendor | Janji temu dan telekonsultasi | X-as-a-Service dengan tim platform |
| Contoh Medikara: tim platform | Platform | 6 dari infrastruktur dan jaringan pusat | CI/CD, GitOps, pemantauan, fondasi cloud | X-as-a-Service ke lima tim |
| Contoh Medikara: tim keamanan aplikasi dan keandalan | Enabling | 2 | Pemindaian, SLO, penanganan insiden | Facilitating, 6 minggu per tim |
| Contoh Medikara: tim integrasi FHIR | Complicated-subsystem | 3 | SATUSEHAT dan BPJS Kesehatan | Collaboration, lalu X-as-a-Service |
| ... | ... | ... | ... | ... |

Pemeriksaan beban kognitif: berapa modul atau layanan yang dipegang setiap tim
stream-aligned, dan berapa yang masih harus diurus sendiri di luar tugas
utamanya? ...

## E. Peta jalan platform internal (tiga sampai lima kapabilitas)

| Urutan | Kapabilitas | Masalah dari bagian A yang diselesaikan | Pengguna pertama | Ukuran keberhasilan | Triwulan |
| --: | :-- | :-- | :-- | :-- | :-- |
| 1 | Contoh Medikara: templat pipeline dan golden path layanan baru | Uji regresi manual 5 hari, rilis manual | Tim pendaftaran dan jadwal | Layanan baru berjalan di staging dalam 1 hari | I |
| 2 | Contoh Medikara: GitOps untuk konfigurasi produksi | Akses ubah langsung, perubahan tanpa jejak | Tim Medikara+ | 0 perubahan produksi di luar Git | I dan II |
| 3 | Contoh Medikara: pemantauan dan log swalayan | Akses log lewat tiket 3 hari | Kelima tim stream-aligned | Akses log tanpa tiket | II |
| 4 | Contoh Medikara: lingkungan uji swalayan dengan IaC | Lingkungan uji lewat tiket 9 hari | Tim farmasi dan laboratorium | Lingkungan uji siap dalam 30 menit | III |
| ... | ... | ... | ... | ... | ... |

## Daftar periksa sebelum diserahkan

- [ ] Alur saat ini memakai data nyata yang dianonimkan, bukan perkiraan rapat.
- [ ] Setiap persetujuan yang dipertahankan punya alasan risiko tertulis.
- [ ] Setiap tim stream-aligned punya aliran nilai yang jelas dan jumlah anggota lima sampai sembilan orang.
- [ ] Setiap kapabilitas platform dikaitkan dengan satu masalah di bagian A.
- [ ] Angka di berkas ini sama dengan angka di presentasi C4.
