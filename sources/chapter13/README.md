# Sumber Bab 13

Berkas pendukung Bab 13, DevOps, GitOps, dan Platform Engineering. Seluruh
angka di dalamnya rekaan untuk kasus fiktif Medikara Health. Berkas dipakai pada
Aktivitas "Model Operasi Delivery dan Peta Jalan Platform Internal", pada kotak
pendalaman teknis, dan pada Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-model-operasi-delivery.md` | Templat luaran Aktivitas: pemetaan alur perubahan saat ini, metrik DORA, alur target CI/CD dan GitOps, topologi tim target, dan peta jalan platform internal. Baris "Contoh Medikara" berisi angka tabel contoh pemetaan alur pada Aktivitas dan gambar topologi tim Medikara di naskah. |
| `contoh-riwayat-deployment.csv` | Contoh riwayat deployment 2025 untuk SIMRS RS Jakarta (7 deployment) dan Medikara+ (14 deployment). Setiap baris mencatat jenis deployment, jumlah perubahan, lead time rata-rata, kegagalan, dan menit pemulihan. |
| `hitung-metrik-dora.py` | Skrip Python (pustaka standar saja) untuk Latihan 1: menghitung frekuensi deployment, lead time perubahan, tingkat kegagalan perubahan, waktu pemulihan, tingkat pengerjaan ulang, dan peluang rilis bermasalah menurut ukuran rilis. |
| `contoh-pipeline-gitops/ci-jadwal-dokter.yml` | Contoh *workflow* GitHub Actions untuk pendalaman teknis: periksa sintaks, bangun *image*, uji asap, lalu kirim *image* ke *registry* dari cabang `main`. |
| `contoh-pipeline-gitops/application-jadwal-dokter.yaml` | Contoh *Application* Argo CD untuk pendalaman teknis: menarik *manifest* dari repositori konfigurasi dan merekonsiliasinya secara otomatis. |

Cara menjalankan skrip:

```bash
cd sources/chapter13
python hitung-metrik-dora.py contoh-riwayat-deployment.csv
```

Argumen kedua yang opsional adalah lama periode pengamatan dalam bulan
(bawaannya 12). Untuk data tim, buat berkas dengan kolom yang sama
(`id_deployment`, `aplikasi`, `tanggal_deploy`, `jenis`, `jumlah_perubahan`,
`lead_time_hari`, `butuh_perbaikan`, `menit_pemulihan`). Kolom `jenis` berisi
`terjadwal` atau `darurat`, dan kolom `butuh_perbaikan` berisi `ya` atau
`tidak`. Baris pertama berkas contoh adalah komentar yang diawali `#`.

Cara memakai contoh pipeline dan GitOps (opsional, hanya di akun dan klaster
latihan milik sendiri):

1. Buat repositori aplikasi berisi `app.py` dan `Dockerfile` dari
   `sources/chapter08/contoh-container`, lalu salin `ci-jadwal-dokter.yml` ke
   `.github/workflows/`. Ganti nilai `IMAGE` dengan nama organisasi sendiri.
2. Buat repositori konfigurasi berisi folder `jadwal-dokter/produksi` dengan
   `deployment.yaml` dan `service.yaml` dari Bab 08. Ganti nilai `image` dengan
   *image* hasil pipeline.
3. Pasang Argo CD di klaster lokal (kind atau minikube) sesuai dokumentasi
   resminya, ganti `repoURL` pada `application-jadwal-dokter.yaml`, lalu
   jalankan `kubectl apply -n argocd -f application-jadwal-dokter.yaml`.
4. Ubah jumlah replika langsung dengan `kubectl scale`, lalu amati Argo CD
   mengembalikannya ke nilai di Git.

Data catatan rilis, tiket, dan struktur tim dari organisasi nyata dipakai
seizin organisasi. Nama orang, data pasien, alamat server, dan kunci akses
dihapus sebelum berkas dibagikan ke anggota tim. Jangan menyimpan token atau
kata sandi di repositori; pakai fitur rahasia (*secrets*) dari layanan Git.
