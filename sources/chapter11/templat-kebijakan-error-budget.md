<!-- Templat kebijakan error budget satu halaman untuk Aktivitas Bab 11. Salin, ganti setiap "...", lalu mintakan tanda tangan semua pihak sebelum ada insiden. -->

# Kebijakan Error Budget: (nama layanan)

Versi: ...
Berlaku sejak: ...
Ditinjau ulang setiap: ... bulan

## 1. Lingkup

- Layanan dan perjalanan pengguna yang dicakup: ...
- SLO yang menjadi dasar (lihat templat SLO): ...
- Jendela: ... hari bergulir.

## 2. Zona dan tindakan

| Sisa anggaran | Status | Tindakan | Yang memutuskan |
| :-- | :-- | :-- | :-- |
| Di atas 50 persen | Normal | ... | ... |
| 25 sampai 50 persen | Waspada | ... | ... |
| Di bawah 25 persen | Fokus keandalan | ... | ... |
| Habis | Beku | ... | ... |

Contoh dari Bab 11 (Medikara Health): di bawah 25 persen hanya perubahan untuk keandalan,
keamanan, atau keselamatan pasien yang boleh dirilis; bila anggaran habis, semua rilis fitur
dihentikan sampai SLI kembali di atas SLO.

## 3. Syarat postmortem

- Satu insiden yang memakan lebih dari ... persen anggaran wajib ditulis postmortem-nya paling
  lambat ... hari kerja setelah insiden.
- Postmortem ditulis tanpa menyalahkan individu dan memuat: ringkasan, dampak dan anggaran
  terpakai, linimasa, penyebab utama dan faktor pendukung, hal yang berjalan baik, hal yang
  berjalan buruk, serta tindak lanjut dengan pemilik dan tenggat.

## 4. Pengecualian

Kebijakan tidak menghentikan rilis bila anggaran habis karena:

- ...
- ...

Kejadian yang dikecualikan tetap dicatat dan dibahas.

## 5. Penyelesaian perselisihan

Perselisihan tentang perhitungan anggaran atau tindakan yang diwajibkan dibawa ke: ...

## 6. Persetujuan

| Peran | Nama | Tanda tangan | Tanggal |
| :-- | :-- | :-- | :-- |
| Pemilik produk | ... | ... | ... |
| Pemimpin teknis | ... | ... | ... |
| Wakil operasi | ... | ... | ... |
| Wakil manajemen | ... | ... | ... |
