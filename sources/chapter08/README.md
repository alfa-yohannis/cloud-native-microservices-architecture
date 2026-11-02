# Sumber Bab 08

Berkas pendukung Aktivitas "Matriks Keputusan Runtime" dan Latihan Bab 08
(Container, Kubernetes, dan Serverless). Seluruh angka contoh adalah rekaan
untuk kasus fiktif Medikara Health, kecuali tarif penyedia yang dirujuk di
naskah bab. Data pasien atau karyawan nyata tidak boleh dimasukkan ke berkas
mana pun di folder ini.

| Berkas | Kegunaan |
| :-- | :-- |
| `matriks-keputusan-runtime.xlsx` | Lembar kerja Aktivitas: petunjuk, kriteria dan bobot, contoh layanan janji temu dan pengingat, lembar isian dengan rumus nilai berbobot, templat ADR singkat, dan kalkulator biaya *serverless* untuk Latihan 1 |
| `contoh-container/app.py` | Layanan jadwal dokter tiruan berbahasa Python, hanya memakai pustaka standar; menjawab `/jadwal` dan `/sehat` |
| `contoh-container/Dockerfile` | Resep membangun *container image* layanan jadwal dokter (Listing Bab 08) |
| `contoh-container/deployment.yaml` | Manifest *deployment* Kubernetes dengan tiga replika dan pemeriksaan kesehatan (Listing Bab 08) |
| `contoh-container/service.yaml` | Manifest *service* Kubernetes yang memberi alamat tetap bagi ketiga *pod* |

## Menjalankan di klaster lokal (pendalaman teknis, opsional)

Prasyarat: Docker, kind, dan kubectl sudah terpasang. Perintah di bawah ini
dikutip pada Listing "Menjalankan layanan jadwal dokter di klaster kind".

```bash
# Jalankan dari folder sources/chapter08/contoh-container.
docker build -t jadwal-dokter:1.0.0 .
kind create cluster --name medikara-lokal
kind load docker-image jadwal-dokter:1.0.0 --name medikara-lokal
kubectl apply -f deployment.yaml -f service.yaml
kubectl get pods -l app=jadwal-dokter
# Hapus satu pod, lalu lihat penggantinya muncul (self-healing).
kubectl delete pod NAMA-POD-DARI-PERINTAH-SEBELUMNYA
kubectl get pods -l app=jadwal-dokter
kubectl port-forward service/jadwal-dokter 8080:80
# Selesai: hapus klaster agar laptop tidak terbebani.
kind delete cluster --name medikara-lokal
```

Sesudah `kubectl port-forward` berjalan, buka `http://localhost:8080/jadwal`.
Pengguna minikube mengganti perintah `kind load docker-image` dengan
`minikube image load jadwal-dokter:1.0.0`.

Peringatan: uji beban untuk melihat *autoscaling* hanya dijalankan pada klaster
lokal milik sendiri atau sistem yang sudah berizin tertulis.
