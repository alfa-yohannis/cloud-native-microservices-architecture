# Sumber Modul

Direktori ini memuat berkas pendukung tiap bab: lembar kerja, templat, data
studi kasus, dan berkas teknis opsional yang dirujuk dari naskah modul.

Susunannya satu subdirektori per bab, dari `chapter01` sampai `chapter14`.
Naskah bab merujuk berkas di sini dengan penulisan seperti
`sources/chapter02/lembar-kerja.md`, sehingga mahasiswa dapat memakai templat
yang sama tanpa menyalin ulang dari halaman cetak. Setiap subdirektori punya
`README.md` berisi daftar berkas dan cara memakainya.

| Bab | Isi | Tonggak |
| --- | --- | --- |
| [01](chapter01/README.md) | Templat profil organisasi, lembar pemicu modernisasi, panduan izin dan anonimisasi | C1 |
| [02](chapter02/README.md) | Templat matriks penempatan *workload*, ringkasan regulasi lokasi data, lembar latihan, skrip katalog region dan zona | C1 |
| [03](chapter03/README.md) | Templat TCO, lembar sasaran nilai, contoh tagihan FOCUS dan skrip pengolahnya | C1 |
| [04](chapter04/README.md) | Lembar penilaian kesiapan CAF, templat inventaris aplikasi, panduan keputusan 7R, data koneksi jaringan dan skrip kelompok pindah | C2 |
| [05](chapter05/README.md) | Kartu skor *twelve-factor*, pertanyaan bukti per faktor, contoh aplikasi konfigurasi | C2 |
| [06](chapter06/README.md) | Panduan fasilitasi EventStorming, templat *context map*, data akses tabel SIMRS dan skrip pencocokan | C2 |
| [07](chapter07/README.md) | Lembar diagnosis *coupling*, data riwayat perubahan dan skrip penghitung, templat ADR, daftar periksa C2 | C2 |
| [08](chapter08/README.md) | Matriks keputusan *runtime*, contoh *container* dan manifest Kubernetes | C3 |
| [09](chapter09/README.md) | Templat peta interaksi dan katalog *event*, spesifikasi AsyncAPI, contoh *broker* lokal | C3 |
| [10](chapter10/README.md) | Templat peta kepemilikan data, templat rancangan saga, contoh *outbox* PostgreSQL | C3 |
| [11](chapter11/README.md) | Templat SLO dan kebijakan *error budget*, kalkulator *error budget*, contoh OpenTelemetry | C3 |
| [12](chapter12/README.md) | Templat analisis dampak bisnis dan rencana DR, skenario *game day*, skrip strategi DR dan simulasi *circuit breaker* | C4 |
| [13](chapter13/README.md) | Templat model operasi *delivery*, data riwayat *deployment* dan skrip metrik DORA, contoh *pipeline* dan GitOps | C4 |
| [14](chapter14/README.md) | Templat peta jalan modernisasi, katalog *guardrail*, templat presentasi C4, contoh Open Policy Agent | C4 |

Seluruh angka dan kejadian di dalam berkas contoh rekaan, mengikuti kasus Medikara
Health. Data pribadi pasien atau karyawan tidak boleh dimasukkan ke templat.