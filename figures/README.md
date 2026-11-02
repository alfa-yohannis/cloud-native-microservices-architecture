# Gambar Modul dan Slide

Folder ini menyimpan gambar yang dipakai bersama oleh modul dan slide, supaya kedua
versi menampilkan gambar yang sama.

- Diagram TikZ `chNN-nama.tex` hanya berisi satu `tikzpicture` tanpa preamble. Modul
  memanggil `\input{../figures/chNN-nama.tex}`, slide memanggil
  `\input{../../figures/chNN-nama.tex}`.
- Ilustrasi JPG `chNN-nama.jpg` tanpa teks di dalam gambar disimpan sebagai arsip dan tidak
  dipasang pada bab atau slide, karena diagram TikZ dan diagram konsep sudah cukup. Prompt
  pembuatannya ada di `illustration-prompts.json`.
- `logo_universitas.png` dan `building.png` adalah berkas asli untuk halaman judul modul
  dan tema slide.

Kolom Isi mengikuti caption gambar di naskah bab.

| Berkas | Dipakai di | Isi |
| --- | --- | --- |
| `ch01-bahasa-bersama.jpg` | Arsip, tidak dipasang | Tim berlatar campuran membahas satu sistem yang sama: rumah sakit, ponsel pasien, server, basis data, dan *cloud* |
| `ch01-capstone.tex` | Bab 1; Slide 1 | Empat mata kuliah menyumbang ke satu cetak biru yang disusun lewat empat tonggak capstone |
| `ch01-perjalanan-mk.tex` | Bab 1; Slide 1 | Perjalanan mata kuliah dalam empat Bagian, dari strategi sampai peta jalan modernisasi |
| `ch01-perjalanan-permintaan.tex` | Bab 1; Slide 1 | Perjalanan satu permintaan janji temu dari Medikara+ sampai ke basis data SIMRS, lalu kembali ke ponsel pasien |
| `ch01-tarik-menarik.tex` | Bab 1; Slide 1 | Lima kualitas sistem yang saling tarik-menarik beserta contoh pertentangannya |
| `ch02-alur-lokasi-data.tex` | Bab 2; Slide 2 | Urutan pertanyaan untuk menentukan lokasi data yang diizinkan bagi satu *workload* |
| `ch02-definisi-nist.tex` | Bab 2; Slide 2 | Struktur definisi *cloud* NIST SP 800-145: lima karakteristik, tiga model layanan, dan empat model penerapan |
| `ch02-lokasi-data.jpg` | Arsip, tidak dipasang | Jaringan layanan kesehatan, pusat data di dalam negeri, dan satu jalur terkunci menuju pusat data di luar negeri |
| `ch02-model-penerapan.tex` | Bab 2; Slide 2 | Empat model penerapan menurut NIST SP 800-145 dan *multi-cloud* sebagai praktik industri |
| `ch02-region-zona.tex` | Bab 2; Slide 2 | *Region* berisi beberapa *availability zone*; pilihan *region* menentukan latensi, ketersediaan, dan lokasi data |
| `ch02-tanggung-jawab.tex` | Bab 2; Slide 2 | Pembagian tanggung jawab per lapisan pada pusat data sendiri, IaaS, PaaS, dan SaaS, disederhanakan dari |
| `ch03-alur-alokasi.tex` | Bab 3; Slide 3 | Alur alokasi biaya: tagihan dinormalisasi, dialokasikan lewat *tag*, diperlihatkan atau dibebankan, lalu dibaca sebagai biaya per unit |
| `ch03-gunung-es-tco.tex` | Bab 3; Slide 3 | TCO sebagai gunung es: harga yang terlihat di penawaran hanya sebagian kecil dari biaya selama masa pakai |
| `ch03-meja-biaya-bersama.jpg` | Arsip, tidak dipasang | Biaya *cloud* dikelola bersama oleh keuangan, tim teknik, dan pimpinan, dengan memperhitungkan nilai layanan dan jejak lingkungannya |
| `ch03-pola-beban-harga.tex` | Bab 3; Slide 3 | Pola beban satu hari menentukan bagian yang ditutup komitmen, *on-demand*, dan *spot* |
| `ch03-siklus-finops.tex` | Bab 3; Slide 3 | Tiga fase FinOps yang berulang dan bermuara pada nilai bisnis teknologi |
| `ch04-landing-zone.tex` | Bab 4; Slide 4 | *Landing zone* rancangan awal Medikara Health: fondasi bersama di bawah, akun per *workload* di tengah, dan CCoE yang menjaga standarnya |
| `ch04-memilah-portofolio.jpg` | Arsip, tidak dipasang | Tim lintas fungsi memilah portofolio aplikasi: sebagian dipindah, sebagian disimpan, sebagian dibangun ulang, dan sebagian dimatikan |
| `ch04-peta-dependensi.tex` | Bab 4; Slide 4 | Sebagian peta dependensi Medikara Health (rekaan). Dua dependensi tersembunyi mengubah susunan kelompok pindah |
| `ch04-pohon-7r.tex` | Bab 4; Slide 4 | Urutan pertanyaan untuk usulan awal 7R. Jawaban pertama yang cocok menentukan usulan; keterangan di kanan diringkas dari kasus pemakaian AWS |
| `ch04-profil-kesiapan.tex` | Bab 4; Slide 4 | Profil kesiapan Medikara Health pada enam perspektif (angka rekaan) dibandingkan dengan batas minimal: skor 3, kecuali Security 4 |
| `ch04-struktur-aws-caf.tex` | Bab 4; Slide 4 | Susunan AWS CAF: enam perspektif berisi *capability* dasar yang mendukung empat domain transformasi, dijalankan dalam empat fase berulang |
| `ch05-definisi-cncf.tex` | Bab 5; Slide 5 | Susunan definisi *cloud-native* CNCF versi 1.1: praktik, contoh teknologi, sifat sistem yang dituju, dan hasil yang diharapkan |
| `ch05-immutable.tex` | Bab 5; Slide 5 | Server yang dirawat menumpuk perubahan manual, sedangkan server *immutable* dibangun ulang dari definisi dan diganti utuh |
| `ch05-loket-kembar.jpg` | Arsip, tidak dipasang | Loket yang sama persis dapat ditambah kapan saja karena tidak ada loket yang menyimpan catatan pasien sendiri |
| `ch05-satu-kode-banyak-deploy.tex` | Bab 5; Slide 5 | Satu *codebase*, satu *build*, lima *release*: yang berbeda antarlokasi hanya konfigurasinya |
| `ch05-sesi-skala.tex` | Bab 5; Slide 5 | Sesi di memori server mengikat pengguna pada satu server, sedangkan proses tanpa *state* berbagi satu penyimpanan sesi |
| `ch05-tiga-kelompok.tex` | Bab 5; Slide 5 | Dua belas faktor dalam tiga kelompok, masing-masing dengan satu pertanyaan bisnis |
| `ch06-context-map.tex` | Bab 6; Slide 6 | *Context map* kondisi saat ini untuk alur rawat jalan Medikara Health |
| `ch06-lokakarya-bersama.jpg` | Arsip, tidak dipasang | Pakar bisnis dan tim teknis menyusun alur layanan bersama, lalu mengelompokkan kejadian menjadi bagian-bagian yang punya bahasa sendiri |
| `ch06-makna-pasien.tex` | Bab 6; Slide 6 | Satu kata "pasien", tiga makna di tiga *bounded context*; yang dibagi hanya identitas penghubung |
| `ch06-papan-eventstorming.tex` | Bab 6; Slide 6 | Papan EventStorming ringkas dari pendaftaran rawat jalan sampai klaim BPJS Kesehatan, dengan *pivotal event* sebagai petunjuk batas *bounded context* |
| `ch06-peta-subdomain.tex` | Bab 6; Slide 6 | Peta *subdomain* awal Medikara Health: tiga *core*, lima *supporting*, dan empat *generic* |
| `ch07-coupling-data.tex` | Bab 7; Slide 7 | *Coupling* data: berbagi tabel membuat satu perubahan kecil merambat ke banyak bagian, sedangkan kepemilikan data menahannya di satu modul |
| `ch07-hukum-conway.tex` | Bab 7; Slide 7 | Hukum Conway pada SIMRS: tim per rumah sakit menghasilkan lima salinan, tim per domain menghasilkan modul per domain |
| `ch07-spektrum-gaya.tex` | Bab 7; Slide 7 | Tiga gaya arsitektur pada satu spektrum: manfaat dan biaya naik bersama, dengan monolit terdistribusi sebagai jebakan |
| `ch07-struktur-adr.tex` | Bab 7; Slide 7 | Susunan satu ADR dan siklus statusnya |
| `ch07-tiga-kawasan.jpg` | Arsip, tidak dipasang | Tiga cara menata satu kawasan: satu gedung besar, satu kompleks bersayap, dan permukiman rumah kecil yang dihubungkan jalan |
| `ch08-alur-serverless.tex` | Bab 8; Slide 8 | Alur FaaS: pemicu menyalakan instans fungsi sesuai kebutuhan, lalu hasilnya dikirim ke layanan tujuan |
| `ch08-pelabuhan-container.jpg` | Arsip, tidak dipasang | Muatan berkemasan standar diatur otomatis ke kapal yang sesuai, sementara tenaga tambahan hanya datang ketika dipanggil |
| `ch08-rekonsiliasi.tex` | Bab 8; Slide 8 | Satu putaran rekonsiliasi: kontroler membandingkan keadaan yang diinginkan dengan keadaan aktual, lalu bertindak sampai keduanya sama |
| `ch08-spektrum-tanggung-jawab.tex` | Bab 8; Slide 8 | Pembagian tanggung jawab pada enam pilihan *runtime*; kolom Kubernetes sendiri diasumsikan berjalan di atas VM sewaan |
| `ch08-vm-container.tex` | Bab 8; Slide 8 | Susunan lapisan pada *virtual machine* dan *container*: VM menggandakan sistem operasi, *container* berbagi satu *kernel* |
| `ch09-antrean-pubsub.tex` | Bab 9; Slide 9 | Antrean pesan membagi pekerjaan di antara penerima (A), sedangkan *publish/subscribe* memberi salinan kepada setiap pelanggan (B) |
| `ch09-koreografi-orkestrasi.tex` | Bab 9; Slide 9 | *Choreography* untuk reaksi atas janji temu dan hasil laboratorium (A), serta *orchestration* untuk proses klaim asuransi (B) |
| `ch09-pos-pemilah-event.jpg` | Arsip, tidak dipasang | Kabar dititipkan ke pos pemilah, lalu klinik, laboratorium, apotek, dan penagihan mengambilnya pada waktu masing-masing |
| `ch09-rantai-sinkron.tex` | Bab 9; Slide 9 | Alur janji temu Medikara+: rantai empat panggilan sinkron (A) dibandingkan dengan rancangan yang hanya menunggu jadwal dokter dan menitipkan sisanya sebagai *event* (B) |
| `ch09-service-mesh.tex` | Bab 9; Slide 9 | *API gateway* di tepi sistem dan *service mesh* untuk lalu lintas antarlayanan, dengan *proxy* di samping setiap layanan |
| `ch10-basis-data-bersama.tex` | Bab 10; Slide 10 | Basis data bersama dibandingkan dengan *database per service* |
| `ch10-lemari-arsip-per-bagian.jpg` | Arsip, tidak dipasang | Setiap bagian memegang lemari arsipnya sendiri, dan kabar perubahan dikirim lewat baki surat keluar |
| `ch10-outbox.tex` | Bab 10; Slide 10 | Alur *transactional outbox* pada Layanan Jadwal |
| `ch10-read-model.tex` | Bab 10; Slide 10 | *Read model* laporan yang dibangun dari *event* layanan operasional |
| `ch10-saga-rujukan.tex` | Bab 10; Slide 10 | Saga pendaftaran pasien rujukan beserta kompensasinya |
| `ch11-alur-insiden.tex` | Bab 11; Slide 11 | Alur penanganan insiden dari deteksi sampai tindak lanjut, dengan empat peran yang dipisahkan selama insiden berlangsung |
| `ch11-alur-opentelemetry.tex` | Bab 11; Slide 11 | Rancangan alur telemetri Medikara Health dengan OpenTelemetry: layanan cukup diinstrumentasi sekali, sedangkan penyimpanannya dapat diganti |
| `ch11-dasbor-hijau.jpg` | Arsip, tidak dipasang | Dasbor tim teknis hijau, tetapi pasien gagal membuat janji temu: ukuran yang dipantau belum menyentuh pengalaman pasien |
| `ch11-sisa-anggaran.tex` | Bab 11; Slide 11 | Sisa *error budget* pemesanan Medikara+ dalam satu jendela 30 hari: dua kejadian memakan 58 persen anggaran, dan kebijakan berlaku setelah sisa di bawah 25 persen |
| `ch11-trace-janji-temu.tex` | Bab 11; Slide 11 | Satu *trace* pemesanan janji temu ke rumah sakit Bandung: dua percobaan ke adaptor SIMRS habis waktu, sehingga aplikasi menyerah sebelum konfirmasi tiba |
| `ch12-cakupan-perlindungan.tex` | Bab 12; Slide 12 | Cakupan perlindungan *multi-AZ*, lokasi kedua, dan cadangan terpisah, beserta kendala lokasi data untuk rekam medis elektronik |
| `ch12-circuit-breaker.tex` | Bab 12; Slide 12 | Tiga keadaan *circuit breaker* dan perilaku yang terasa oleh petugas loket |
| `ch12-kegagalan-berantai.tex` | Bab 12; Slide 12 | Kegagalan berantai: layanan pihak ketiga yang melambat menghabiskan kolam koneksi, lalu merambat sampai ke antrean loket pendaftaran |
| `ch12-rto-rpo.tex` | Bab 12; Slide 12 | RPO diukur mundur dari bencana ke titik pemulihan terakhir; RTO diukur maju dari bencana sampai layanan kembali melayani |
| `ch12-rumah-sakit-tetap-menyala.jpg` | Arsip, tidak dipasang | Rumah sakit tetap menyala ketika kota di sekitarnya padam: resiliensi berarti layanan inti terus berjalan saat sebagian infrastruktur gagal |
| `ch12-strategi-dr.tex` | Bab 12; Slide 12 | Empat strategi DR: makin ke kanan, lokasi kedua makin siap, RTO dan RPO makin pendek, dan biayanya makin tinggi |
| `ch13-antrean-dan-jalur.jpg` | Arsip, tidak dipasang | Dua cara mengirim perubahan: tumpukan berkas yang menunggu banyak meja persetujuan dan jalur otomatis yang mengirim paket kecil secara rutin |
| `ch13-lapisan-platform.tex` | Bab 13; Slide 13 | Lapisan platform internal Medikara: tim *stream-aligned* memakai antarmuka swalayan di atas kapabilitas dan fondasi yang dikelola tim platform |
| `ch13-pipeline-cicd.tex` | Bab 13; Slide 13 | Tahap *pipeline* CI/CD dan cakupan *continuous integration*, *continuous delivery*, serta *continuous deployment* |
| `ch13-siklus-gitops.tex` | Bab 13; Slide 13 | Siklus GitOps: perubahan diusulkan lewat Git, ditarik agen, dan direkonsiliasi terus dengan keadaan aktual klaster |
| `ch13-topologi-tim-medikara.tex` | Bab 13; Slide 13 | Topologi tim target TI Medikara: lima tim *stream-aligned* didukung tim platform, tim *enabling*, dan tim *complicated-subsystem* |
| `ch14-gelombang.tex` | Bab 14; Slide 14 | Tiga gelombang modernisasi Medikara Health, April 2027 sampai September 2030, dengan gerbang keputusan di antara gelombang |
| `ch14-guardrail-pac.tex` | Bab 14; Slide 14 | *Policy as code* dalam alur perubahan: pemeriksaan proaktif di *pipeline*, penolakan preventif di tingkat akun, dan pemindaian detektif sesudah sumber daya berjalan |
| `ch14-peta-jalan.jpg` | Arsip, tidak dipasang | Peta jalan sebagai perjalanan bertahap: gedung lama tetap melayani pasien selama jalan menuju kampus baru dibangun, dengan pagar pengaman di setiap tikungan |
| `ch14-siklus-operate.tex` | Bab 14; Slide 14 | Siklus fase Operate di Medikara Health: anggaran, pemantauan, deteksi anomali, penyelidikan, tindakan, dan tinjauan biaya per unit, dengan tag wajib sebagai pusat data |
| `ch14-strangler-fig.tex` | Bab 14; Slide 14 | Tiga tahap *strangler fig* untuk fungsi janji temu: fasad dipasang, permintaan dipindah per rumah sakit, lalu modul janji temu SIMRS dinonaktifkan |
