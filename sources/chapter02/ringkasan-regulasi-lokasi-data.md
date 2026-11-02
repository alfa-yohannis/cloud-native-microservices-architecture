<!-- Ringkasan aturan lokasi data untuk Aktivitas dan Latihan 2 Bab 02. Baca sebagai titik awal, lalu cek teks resmi di JDIH sebelum mengutip. -->

# Ringkasan Regulasi Lokasi Data

Ringkasan ini dipakai anggota tim berlatar hukum, kesehatan, atau bisnis saat mengisi kolom
"Aturan yang mengikat" dan "Lokasi data yang diizinkan" pada matriks kendala penempatan
*workload*. Isinya parafrase, bukan kutipan resmi dan bukan nasihat hukum. Status diperiksa
pada 30 Oktober 2026. Sebelum dikutip di laporan capstone, setiap pasal dicek ulang di JDIH
(Jaringan Dokumentasi dan Informasi Hukum) atau di <https://peraturan.bpk.go.id>.

## Urutan pemeriksaan

Aturan dibaca berlapis. Lapisan yang paling ketat menentukan hasil akhir.

1. Siapa penyelenggara sistemnya: lingkup publik atau lingkup privat (PP 71/2019).
2. Apakah *workload* menyimpan data kesehatan atau rekam medis elektronik (PP 28/2024 dan
   Permenkes 24/2022).
3. Apakah *workload* mengolah data pribadi, dan apakah ada data pribadi spesifik seperti
   data kesehatan (UU 27/2022 dan PP 33/2026).
4. Apakah ada aturan sektor atau kontrak lain, misalnya perjanjian kerja sama dengan BPJS
   Kesehatan, syarat mitra asuransi, atau kebijakan internal.

## PP 71/2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik

Sumber: <https://peraturan.bpk.go.id/Details/122030/pp-no-71-tahun-2019>. Status: berlaku;
rencana revisi masih dievaluasi Komdigi.

- **Pasal 20 (lingkup publik).** Pengelolaan, pemrosesan, dan penyimpanan sistem dan data
  elektronik wajib di wilayah Indonesia. Pengecualian hanya bila teknologi penyimpanannya
  tidak tersedia di dalam negeri, menurut kriteria komite yang dibentuk menteri. Bila
  memakai layanan pihak ketiga, data wajib diklasifikasikan berdasarkan risiko.
- **Pasal 21 (lingkup privat).** Boleh di dalam maupun di luar wilayah Indonesia. Bila di
  luar negeri, penyelenggara wajib memastikan efektivitas pengawasan oleh kementerian atau
  lembaga dan penegakan hukum, serta wajib memberi akses ke sistem dan data untuk keperluan
  itu. Sektor keuangan diatur lebih lanjut oleh otoritas sektor keuangan.

Medikara Health adalah badan usaha swasta, sehingga termasuk lingkup privat. Pasal 21 adalah
aturan umum. Untuk data kesehatan, PP 28/2024 di bawah ini lebih khusus.

## PP 28/2024 tentang Pelaksanaan UU 17/2023 tentang Kesehatan

Sumber: <https://peraturan.bpk.go.id/Details/294077>. Status: berlaku. Pembacaan mengikuti
IT40813 Bab 3.

- **Pasal 966 ayat (2).** Pangkalan data kesehatan berupa pusat data yang berada di dalam
  wilayah Indonesia.
- **Pasal 966 ayat (5).** Jasa pihak lain boleh dipakai bila dilaksanakan di dalam wilayah
  Indonesia, berdasarkan perjanjian kerja sama, dengan data yang dimiliki dan dikendalikan
  penuh oleh penyelenggara.
- **Pasal 972.** Transfer ke luar wilayah hukum untuk tujuan spesifik dan terbatas, dengan izin
  Menteri, serta memenuhi syarat transfer data pribadi.

Pasal 966 tidak menyebut lokasi cadangan secara tersendiri. Perlakuan cadangan sebagai bagian
dari penyimpanan adalah penafsiran, dan kasus nyata tetap perlu dinilai penasihat hukum.

## Permenkominfo 5/2020 tentang PSE Lingkup Privat

Sumber: <https://peraturan.bpk.go.id/Details/203049>. Status: berlaku, diubah dengan
Permenkominfo 10/2021.

- Penyelenggara lingkup privat wajib mendaftarkan sistem elektroniknya.
- Penyelenggara wajib memberi akses ke sistem dan data elektronik untuk pengawasan dan
  penegakan hukum.

## Permenkes 24/2022 tentang Rekam Medis

Sumber: <https://peraturan.bpk.go.id/Details/245544>. Status: berlaku.

- **Pasal 20.** Rekam medis elektronik disimpan pada media digital. Penyimpanan harus
  menjamin keamanan, keutuhan, kerahasiaan, dan ketersediaan data. Media yang diakui:
  server, komputasi awan (*cloud computing*) yang tersertifikasi sesuai peraturan
  perundang-undangan, atau media digital lain yang diakui. Fasilitas wajib punya cadangan
  data yang disimpan di tempat berbeda, dibuat berkala, dan diatur dalam standar prosedur
  operasional.
- **Pasal 39.** Masa simpan paling singkat 25 tahun sejak kunjungan terakhir pasien.

Pertanyaan yang belum dijawab pasal itu sendiri: sertifikasi *cloud* apa yang dimaksud, dan
siapa yang menerbitkannya. Minta konfirmasi tertulis, jangan diasumsikan.

## UU 27/2022 tentang Pelindungan Data Pribadi dan PP 33/2026

Sumber UU: <https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022>. Status: berlaku
penuh sejak Oktober 2024.

- Data dan informasi kesehatan termasuk data pribadi yang bersifat spesifik.
- **Pasal 56.** Transfer data pribadi ke luar wilayah hukum Indonesia: negara tujuan harus
  punya pelindungan setara atau lebih tinggi; bila tidak, harus ada pelindungan yang memadai
  dan mengikat; bila keduanya tidak terpenuhi, harus ada persetujuan subjek data.
- Organisasi yang menentukan tujuan pemrosesan adalah pengendali data. Kewajibannya tetap
  melekat walaupun pemrosesan dikerjakan vendor atau penyedia *cloud*.

PP 33/2026 adalah aturan pelaksana UU PDP. Menurut ringkasan firma hukum, PP ini
ditetapkan 16 Juli 2026 dan berlaku 16 Januari 2027. Teks resminya perlu dibaca di JDIH
sebelum dikutip. Pembahasan rinci ada di IT40813.

## Daftar periksa per workload

| Pertanyaan | Jawaban | Dasar |
| --- | --- | --- |
| Lingkup penyelenggara (publik atau privat)? | ... | PP 71/2019 Pasal 20 atau 21 |
| Ada data kesehatan atau rekam medis elektronik? | ... | PP 28/2024 Pasal 966 dan 972; Permenkes 24/2022 Pasal 20 dan 39 |
| Ada data pribadi? Ada data spesifik? | ... | UU 27/2022 |
| Data keluar negeri? Apa dasar transfernya? | ... | UU 27/2022 Pasal 56 |
| Ada kontrak atau aturan sektor lain? | ... | Perjanjian kerja sama, kebijakan internal |
| Pertanyaan yang belum terjawab dan penelusurnya | ... | ... |
