<!-- Templat SLO layanan kritis untuk Aktivitas Bab 11. Salin berkas ini, isi satu baris per perjalanan pengguna, lalu lampirkan ke dokumen C3. -->

# Templat SLO Layanan Kritis

Organisasi: ...
Tim: ...
Tanggal: ...

Catatan pengisian:

- Tulis SLI sebagai rasio: peristiwa baik dibagi seluruh peristiwa.
- Ukur sedekat mungkin dengan pengguna, misalnya di API gateway atau di aplikasi.
- Hitung error budget dalam menit dan dalam jumlah permintaan. Kalkulator tersedia di
  `hitung_error_budget.py`.
- Jangan mencatat data pribadi pasien atau karyawan sebagai bagian dari telemetri.

## 1. Perjalanan pengguna kritis

| No | Perjalanan | Pengguna | Seberapa sering dipakai | Dampak bila gagal |
| :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

## 2. SLI, SLO, dan error budget

| No | SLI: peristiwa baik / seluruh peristiwa | Titik ukur | SLO | Jendela | Volume per jendela | Error budget (menit) | Error budget (permintaan) |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... | ... |

Contoh baris dari Bab 11:

| No | SLI: peristiwa baik / seluruh peristiwa | Titik ukur | SLO | Jendela | Volume per jendela | Error budget (menit) | Error budget (permintaan) |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | Upaya pemesanan yang terkonfirmasi dalam 5 detik / seluruh upaya yang sah | API gateway dan aplikasi | 99,5% | 30 hari bergulir | sekitar 28.000 | 216 | 140 |

## 3. Kebutuhan telemetri

| No | Metrik untuk SLI | Trace yang dibutuhkan | Log yang dibutuhkan | Data yang wajib disamarkan atau tidak dicatat |
| :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

## 4. Alert

| No | Laju pembakaran | Jendela panjang | Jendela pendek | Pemberitahuan | Penerima |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 14,4 | 1 jam | 5 menit | Panggil petugas jaga | ... |
| 2 | 6 | 6 jam | 30 menit | Panggil petugas jaga | ... |
| 3 | 1 | 3 hari | 6 jam | Tiket | ... |

## 5. Persetujuan

| Peran | Nama | Tanggal |
| :-- | :-- | :-- |
| Pemilik layanan | ... | ... |
| Pemimpin teknis | ... | ... |
| Wakil manajemen | ... | ... |
