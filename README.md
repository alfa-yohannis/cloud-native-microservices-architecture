# Cloud-Native & Microservices Architecture

IT40713 · Magister Teknologi Informasi, peminatan Digital Enterprise Architecture, Universitas Pradita.

Mata kuliah ini membahas cara organisasi memindahkan, membangun, dan menjalankan sistem informasinya di *cloud* dengan memperhitungkan biaya, risiko, dan regulasi. Setiap pembahasan berangkat dari masalah organisasi yang nyata, misalnya layanan yang sering tidak tersedia, biaya integrasi yang membengkak, atau perubahan aplikasi yang memakan waktu berbulan-bulan. Setelah masalahnya jelas, barulah konsep dan istilah teknis diperkenalkan: model layanan *cloud*, ekonomi *cloud*, prinsip *cloud-native*, *microservices*, *container*, *event-driven architecture*, DevOps, *observability*, dan *platform engineering*. Sasarannya bukan kemampuan memprogram, melainkan kemampuan menimbang pilihan arsitektur, membaca *trade-off*, dan menuliskan justifikasi keputusan yang dapat dipertanggungjawabkan di depan manajemen.

Kelas ini berisi mahasiswa berlatar campuran. Mahasiswa berlatar bisnis, manajemen, akuntansi, hukum, kesehatan, dan bidang lain tidak dituntut bisa memprogram. Mahasiswa berlatar CS (*Computer Science*), SE (*Software Engineering*), atau TI (teknologi informasi) mendapat pendalaman teknis opsional di setiap pertemuan. IT40713 dijalankan bersama tiga mata kuliah lain sebagai satu proyek capstone, yaitu penyusunan Cetak Biru Transformasi Digital untuk satu organisasi nyata: [IT40513 Enterprise Architecture & Digital Blueprint](https://github.com/alfa-yohannis/enterprise-architecture-digital-blueprint), [IT40613 Digital Platform & API Economy](https://github.com/alfa-yohannis/digital-platform-api-economy), dan [IT40813 IT Governance, Risk & Compliance](https://github.com/alfa-yohannis/it-governance-risk-compliance). Bagian cetak biru yang menjadi tanggung jawab mata kuliah ini adalah strategi *cloud*, penilaian portofolio aplikasi, arsitektur target berbasis *cloud-native*, serta rencana operasi dan modernisasinya. Tatap muka hanya berlangsung hari Sabtu untuk membahas progres proyek, sehingga modul dan slide disusun agar dapat dipelajari mandiri.

## Peta Pertemuan

Urutan pertemuan mengikuti empat tonggak capstone. Tiga pertemuan pertama membangun bahasa bersama dan konteks strategi. Empat pertemuan berikutnya dipakai untuk membaca kondisi saat ini sebelum UTS (Ujian Tengah Semester). Setelah UTS, tim merancang arsitektur target, lalu menutup semester dengan rencana operasi, peta jalan modernisasi, dan tata kelolanya menjelang UAS (Ujian Akhir Semester). Kolom terakhir menunjukkan artefak yang disumbangkan ke tonggak capstone.

| # | Pertemuan | Aktivitas | Luaran Capstone |
| --- | --- | --- | --- |
| 1 | **Orientasi dan Bahasa Bersama Cloud-Native** | Membentuk tim campuran, memilih organisasi, dan memetakan masalah teknologi informasi yang dirasakan | C1: profil organisasi dan daftar pemicu modernisasi |
| 2 | Model Layanan, Model Penerapan, dan Lokasi Data | Memetakan *workload* ke model layanan dan model penerapan dengan memperhitungkan aturan lokasi data | C1: matriks kendala penempatan *workload* |
| 3 | Ekonomi Cloud, FinOps, dan Keberlanjutan | Menyusun perkiraan TCO (*Total Cost of Ownership*) kasar dan metrik biaya per unit layanan | C1: model biaya awal dan sasaran nilai *cloud* |
| 4 | Kerangka Adopsi Cloud dan Strategi Migrasi 7R | Menilai kesiapan dengan enam perspektif CAF (*Cloud Adoption Framework*) dan memberi usulan 7R untuk setiap aplikasi | C2: penilaian kesiapan dan portofolio aplikasi 7R |
| 5 | Prinsip Cloud-Native dan Twelve-Factor App | Menilai dua sampai tiga aplikasi inti dengan kartu skor *twelve-factor* | C2: kartu skor kesenjangan *cloud-native* |
| 6 | Domain-Driven Design dan Batas Layanan | Menjalankan lokakarya EventStorming untuk satu alur layanan pasien | C2: peta domain dan *context map* kondisi saat ini |
| 7 | Monolit, Modular Monolith, dan Microservices | Mendiagnosis keterkaitan pada aplikasi inti dan menulis ADR (*Architecture Decision Record*) pertama | C2: diagnosis arsitektur dan ADR gaya arsitektur, ditinjau menjelang UTS |
| 8 | Container, Kubernetes, dan Serverless | Memilih *runtime* untuk setiap kandidat layanan dengan matriks keputusan | C3: matriks keputusan *runtime* per layanan |
| 9 | Komunikasi Antarlayanan dan Event-Driven Architecture | Memodelkan alur janji temu sebagai rangkaian *event* | C3: peta interaksi layanan dan katalog *event* |
| 10 | Data dalam Microservices: Saga dan Outbox | Merancang kepemilikan data dan satu saga lintas layanan | C3: peta kepemilikan data dan rancangan saga |
| 11 | Observability, SRE, dan SLO | Menetapkan SLI (*Service Level Indicator*), SLO (*Service Level Objective*), dan *error budget* untuk perjalanan pasien yang kritis | C3: SLO layanan kritis dan rancangan *observability* |
| 12 | Resiliensi dan Disaster Recovery | Menetapkan RTO (*Recovery Time Objective*), RPO (*Recovery Point Objective*), dan strategi pemulihan per layanan | C4: rencana resiliensi dan DR (*Disaster Recovery*) |
| 13 | DevOps, GitOps, dan Platform Engineering | Memetakan alur perubahan dan merancang topologi tim serta platform internal | C4: model operasi *delivery* dan peta jalan platform internal |
| 14 | Peta Jalan Modernisasi dan Tata Kelola Cloud | Menyusun gelombang modernisasi bergaya *strangler fig* beserta *guardrail* tata kelolanya | C4: peta jalan modernisasi dan presentasi capstone |

Pertemuan dikelompokkan ke dalam empat Bagian, satu Bagian untuk satu tonggak. **Bagian I** (Pertemuan 1 sampai 3) menyiapkan C1: alasan organisasi melirik *cloud*, batasan regulasi yang mengikat, dan gambaran biayanya. **Bagian II** (Pertemuan 4 sampai 7) menyiapkan C2: portofolio aplikasi dinilai dengan kacamata kesiapan, prinsip *cloud-native*, batas domain, dan gaya arsitektur. Artefaknya ditinjau menjelang UTS. **Bagian III** (Pertemuan 8 sampai 11) menyiapkan C3: *runtime*, pola komunikasi, kepemilikan data, dan target keandalan untuk arsitektur target. **Bagian IV** (Pertemuan 12 sampai 14) menyiapkan C4: cara sistem dipulihkan, cara perubahan dikirim, dan urutan modernisasi beserta *guardrail* tata kelolanya. Hasilnya dipresentasikan menjelang UAS. Topik yang menjadi milik mata kuliah lain hanya disinggung singkat dan diberi keterangan tempat pembahasan rincinya.

---

## Rencana Pertemuan

### Bagian I. Fondasi dan Strategi Cloud (1 sampai 3)

#### Pertemuan 01 · Orientasi dan Bahasa Bersama Cloud-Native

**Tujuan.**
1. Menjelaskan dengan bahasa sehari-hari istilah dasar sistem informasi: aplikasi, *server*, basis data, jaringan, pusat data, dan *cloud*.
2. Mengaitkan keputusan teknologi dengan nilai bisnis, biaya, risiko, dan regulasi.
3. Merumuskan masalah teknologi informasi di organisasi pilihan tim sebagai pemicu modernisasi.

**Topik.** Cara kerja mata kuliah, tatap muka Sabtu, dan proyek capstone bersama tiga mata kuliah lain. Bahasa bersama bagi mahasiswa non-teknis: aplikasi, *server*, basis data, jaringan, pusat data, dan *cloud*. Bahasa bersama bagi mahasiswa teknis: nilai bisnis, struktur biaya, risiko, dan kepatuhan. Kualitas sistem yang saling tarik-menarik: ketersediaan, skalabilitas, keamanan, biaya, dan kecepatan perubahan. Arti *cloud-native* bagi organisasi dan mitos yang sering menyertainya.

**Aktivitas.** Tim campuran dibentuk, berisi tiga sampai lima orang dengan sedikitnya satu anggota berlatar teknis dan satu anggota berlatar non-teknis. Tim memilih organisasi nyata, sebaiknya tempat kerja salah satu anggota, dengan izin dan data yang dianonimkan. Tim yang tidak punya akses memakai kasus Medikara Health. Anggota non-teknis memimpin wawancara singkat atau penelusuran dokumen tentang masalah layanan yang dirasakan pengguna dan manajemen. Anggota teknis memetakan sistem yang terlibat dalam setiap masalah. Luarannya adalah profil organisasi satu halaman dan daftar lima sampai sepuluh pemicu modernisasi, misalnya antrean panjang, aplikasi yang sering tidak tersedia, atau biaya integrasi yang tinggi. *Pendalaman teknis (opsional):* membuat akun *free tier* di satu penyedia *cloud*, lalu menelusuri konsol dan kalkulator harganya tanpa menjalankan sumber daya berbayar.

**Latihan.**
1. Jelaskan perbedaan antara aplikasi yang sekadar dipindahkan ke *cloud* dan aplikasi *cloud-native*, dengan satu contoh dari tempat kerja atau dari Medikara Health.
2. Pilih satu masalah layanan di Medikara Health, misalnya antrean pendaftaran yang panjang. Uraikan sisi bisnisnya (dampak pada pasien dan pendapatan) dan sisi teknisnya (sistem yang terlibat).
3. Sebutkan dua kualitas sistem yang saling tarik-menarik, misalnya biaya dan ketersediaan, lalu jelaskan mengapa keduanya sulit dimaksimalkan sekaligus.

#### Pertemuan 02 · Model Layanan, Model Penerapan, dan Lokasi Data

**Tujuan.**
1. Membedakan karakteristik esensial, model layanan, dan model penerapan *cloud* menurut NIST (National Institute of Standards and Technology) SP 800-145.
2. Menjelaskan pembagian tanggung jawab antara penyedia dan pelanggan pada IaaS, PaaS, dan SaaS.
3. Menganalisis pengaruh aturan lokasi data di Indonesia terhadap pilihan penempatan *workload*.

**Topik.** Lima karakteristik esensial *cloud* menurut NIST SP 800-145. Model layanan IaaS (*Infrastructure as a Service*), PaaS (*Platform as a Service*), dan SaaS (*Software as a Service*). *Shared responsibility model*. Model penerapan *public*, *private*, *hybrid*, dan *community cloud*, ditambah *multi-cloud*. Region dan AZ (*availability zone*). Region *cloud* yang sudah beroperasi di Indonesia. Lokasi data dan kedaulatan data dalam Peraturan Pemerintah (PP) 71/2019 tentang PSTE (Penyelenggaraan Sistem dan Transaksi Elektronik), Peraturan Menteri Komunikasi dan Informatika (Permenkominfo) 5/2020 tentang PSE (Penyelenggara Sistem Elektronik) Lingkup Privat, dan Peraturan Menteri Kesehatan (Permenkes) 24/2022 tentang Rekam Medis. Undang-Undang (UU) 27/2022 tentang PDP (Pelindungan Data Pribadi) dan PP 33/2026 sebagai aturan pelaksananya disinggung singkat (dibahas rinci di IT40813). Risiko pihak ketiga dan *cloud* juga disinggung singkat (dibahas rinci di IT40813).

**Aktivitas.** Tim mendaftar delapan sampai dua belas *workload* organisasi, misalnya SIMRS (Sistem Informasi Manajemen Rumah Sakit), ERP (*Enterprise Resource Planning*) keuangan, aplikasi pasien, sistem laboratorium, surel, dan pelaporan manajemen. Anggota berlatar hukum, kesehatan, atau bisnis menelusuri jenis data dan aturan yang mengikat setiap *workload*. Anggota teknis menilai model layanan dan model penerapan yang masuk akal. Hasilnya disatukan dalam satu matriks: *workload*, jenis data, aturan yang berlaku, model layanan, model penerapan, dan lokasi data yang diizinkan. Luarannya adalah matriks kendala penempatan *workload* untuk C1. *Pendalaman teknis (opsional):* membandingkan katalog layanan di region Jakarta pada dua penyedia, lalu mencatat layanan yang belum tersedia di region tersebut.

**Latihan.**
1. Klasifikasikan lima layanan yang dipakai sehari-hari di tempat kerja ke dalam IaaS, PaaS, atau SaaS, lalu tunjukkan tanggung jawab keamanan yang tetap dipegang organisasi.
2. Medikara Health ingin menyimpan cadangan rekam medis elektronik di region luar negeri karena harganya lebih murah. Analisis pertanyaan regulasi dan risiko yang harus terjawab sebelum keputusan diambil.
3. Bandingkan *hybrid cloud* dan *multi-cloud* dari sisi biaya, keterampilan tim, dan ketergantungan pada penyedia.

#### Pertemuan 03 · Ekonomi Cloud, FinOps, dan Keberlanjutan

**Tujuan.**
1. Membandingkan struktur biaya pusat data sendiri dan *cloud* dengan pendekatan TCO.
2. Menjelaskan prinsip, fase, dan peran dalam FinOps Framework 2026.
3. Merumuskan metrik biaya per unit dan metrik jejak karbon untuk satu layanan.

**Topik.** CapEx (*Capital Expenditure*) dan OpEx (*Operational Expenditure*). TCO (*Total Cost of Ownership*) dan biaya yang sering terlupa: lisensi, tenaga kerja, migrasi, dan biaya transfer data keluar (*egress*). Model harga *on-demand*, komitmen pemakaian, dan kapasitas *spot*. FinOps Framework 2026: enam prinsip, fase Inform, Optimize, dan Operate, *persona*, domain, *capability*, dan *scope*. Alokasi biaya lewat *tagging*, *showback*, dan *chargeback*. Spesifikasi FOCUS (*FinOps Open Cost and Usage Specification*). *Unit economics*, misalnya biaya infrastruktur per kunjungan pasien. Keberlanjutan: jejak karbon *workload*, pilihan region, dan SCI (*Software Carbon Intensity*) dalam ISO/IEC 21031:2024. *Business case* dan portofolio inisiatif disinggung singkat (dibahas rinci di IT40513).

**Aktivitas.** Tim menyusun perkiraan TCO kasar untuk satu *workload* dari matriks Pertemuan 2, lalu membandingkan kondisi sekarang dengan satu atau dua opsi *cloud*. Anggota berlatar akuntansi atau keuangan memimpin penyusunan struktur biaya dan asumsinya. Anggota teknis memakai kalkulator harga penyedia untuk memperkirakan biaya sumber daya. Tim lalu menetapkan satu metrik biaya per unit dan satu sasaran nilai, misalnya "biaya infrastruktur per kunjungan pasien turun 15 persen dalam dua tahun". Luarannya adalah model biaya awal dan sasaran nilai *cloud* untuk C1. *Pendalaman teknis (opsional):* membaca contoh data tagihan berformat FOCUS, lalu mengelompokkan biaya menurut *tag* layanan dan lingkungan.

**Latihan.**
1. Jelaskan mengapa tagihan *cloud* sebuah organisasi bisa naik walaupun jumlah penggunanya tetap. Berikan tiga penyebab yang mungkin.
2. Pilih satu layanan Medikara Health dan usulkan metrik biaya per unit yang bermakna bagi direksi. Jelaskan alasan pemilihannya.
3. Kapan model harga berbasis komitmen lebih menguntungkan daripada *on-demand*, dan kapan justru merugikan?

### Bagian II. Menilai Kondisi Saat Ini (4 sampai 7)

#### Pertemuan 04 · Kerangka Adopsi Cloud dan Strategi Migrasi 7R

**Tujuan.**
1. Membandingkan struktur kerangka adopsi *cloud* dari AWS (Amazon Web Services), Microsoft, dan Google.
2. Menilai kesiapan organisasi dengan enam perspektif AWS CAF.
3. Memberi usulan strategi 7R yang beralasan untuk setiap aplikasi dalam portofolio.

**Topik.** CAF (*Cloud Adoption Framework*) dari tiga penyedia: AWS CAF dengan enam perspektif, Microsoft CAF dengan fase Strategy, Plan, Ready, Adopt, Govern, Secure, dan Manage, serta Google Cloud Adoption Framework dengan tema Learn, Lead, Scale, dan Secure. Penilaian kesiapan *cloud* dengan perspektif Business, People, Governance, Platform, Security, dan Operations. Inventaris portofolio aplikasi dan pemetaan dependensi. Strategi migrasi 7R: Retire, Retain, Rehost, Relocate, Repurchase, Replatform, dan Refactor. *Landing zone* sebagai fondasi. CCoE (*Cloud Center of Excellence*). Prinsip arsitektur dan *gap analysis* disinggung singkat (dibahas rinci di IT40513).

**Aktivitas.** Tim mengisi lembar penilaian kesiapan untuk enam perspektif CAF. Anggota non-teknis memimpin perspektif Business, People, dan Governance. Anggota teknis memimpin perspektif Platform, Security, dan Operations. Tim lalu menginventaris aplikasi organisasi beserta pemilik, pengguna, dependensi, dan kondisinya, kemudian memberi usulan 7R awal disertai alasan satu kalimat untuk setiap aplikasi. Luarannya adalah penilaian kesiapan *cloud* dan portofolio aplikasi dengan usulan 7R untuk C2. *Pendalaman teknis (opsional):* menggambar diagram dependensi antaraplikasi dari data integrasi, lalu menandai kelompok aplikasi yang harus dipindahkan bersamaan.

**Latihan.**
1. Jelaskan mengapa panduan AWS menyarankan agar strategi Refactor tidak dipakai untuk sebagian besar aplikasi dalam migrasi berskala besar.
2. Medikara Health memiliki SIMRS dengan versi berbeda di lima rumah sakit. Usulkan strategi 7R untuk SIMRS, lalu pertahankan usulan tersebut terhadap satu alternatif lain.
3. Perspektif CAF mana yang paling sering diabaikan ketika migrasi hanya digerakkan oleh divisi TI? Jelaskan akibatnya.

#### Pertemuan 05 · Prinsip Cloud-Native dan Twelve-Factor App

**Tujuan.**
1. Menjelaskan definisi *cloud-native* menurut CNCF (Cloud Native Computing Foundation) dan perbedaannya dengan aplikasi yang sekadar *cloud-hosted*.
2. Menerjemahkan dua belas faktor Twelve-Factor App ke dalam dampak bisnis yang mudah dipahami.
3. Menilai kesenjangan aplikasi yang ada terhadap prinsip *cloud-native*.

**Topik.** Definisi *cloud-native* versi 1.1 dari CNCF. Perbedaan *cloud-hosted* dan *cloud-native*. Twelve-Factor App dan statusnya sebagai dokumen *open source* sejak 2024. Faktor tentang kode, dependensi, konfigurasi, dan *backing service*. Faktor tentang *build*, proses tanpa *state*, konkurensi, dan *disposability*. Faktor tentang kesamaan lingkungan, *log*, dan tugas administratif. Penskalaan vertikal dan horizontal. *Immutable infrastructure* dan konfigurasi deklaratif.

**Aktivitas.** Tim memilih dua sampai tiga aplikasi inti, misalnya SIMRS, Medikara+, dan sistem laboratorium, lalu menilainya dengan kartu skor *twelve-factor*. Anggota teknis menjelaskan arti setiap faktor dan mengumpulkan bukti dari dokumentasi atau wawancara dengan tim TI. Anggota non-teknis menuliskan dampak bisnis dari setiap kesenjangan, misalnya "konfigurasi yang berbeda di setiap rumah sakit membuat satu pembaruan memakan waktu dua minggu". Luarannya adalah kartu skor kesenjangan *cloud-native* untuk aplikasi inti sebagai bagian C2. *Pendalaman teknis (opsional):* mengubah aplikasi contoh kecil agar membaca konfigurasi dari *environment variable* dan menulis *log* ke `stdout`.

**Latihan.**
1. Medikara+ sering lambat setiap kali program vaksinasi diumumkan. Faktor mana dalam Twelve-Factor App yang paling relevan untuk masalah ini? Jelaskan alasannya.
2. Jelaskan dengan bahasa non-teknis mengapa aplikasi yang menyimpan sesi pengguna di memori *server* sulit diskalakan.
3. Apakah semua aplikasi organisasi perlu memenuhi dua belas faktor? Berikan satu contoh aplikasi yang tidak perlu dan jelaskan alasannya.

#### Pertemuan 06 · Domain-Driven Design dan Batas Layanan

**Tujuan.**
1. Mengidentifikasi *core*, *supporting*, dan *generic subdomain* dalam sebuah organisasi.
2. Memfasilitasi lokakarya EventStorming untuk menemukan *bounded context*.
3. Menyusun *context map* yang menunjukkan hubungan antar-*bounded context*.

**Topik.** DDD (*Domain-Driven Design*) sebagai cara memahami bisnis sebelum memecah sistem. Domain dan *subdomain*: *core*, *supporting*, dan *generic*. *Ubiquitous language*. *Bounded context*. *Context map* dan pola hubungannya: *customer-supplier*, *conformist*, *anticorruption layer*, *shared kernel*, dan *open host service*. EventStorming sebagai lokakarya kolaboratif. Heuristik menurunkan kandidat layanan dari *bounded context*. Kaitan dengan *capability map* disinggung singkat (dibahas rinci di IT40513).

**Aktivitas.** Tim menjalankan lokakarya EventStorming untuk satu alur layanan pasien, misalnya dari pendaftaran rawat jalan sampai klaim BPJS Kesehatan. Anggota yang memahami proses bisnis, terutama yang berlatar kesehatan atau manajemen, berperan sebagai pakar domain. Anggota teknis berperan sebagai fasilitator dan pencatat istilah. Tim mengelompokkan *event* menjadi *bounded context*, lalu menggambar *context map* kondisi saat ini, termasuk hubungan dengan BPJS Kesehatan dan SATUSEHAT. Luarannya adalah peta domain dan *context map* kondisi saat ini untuk C2. *Pendalaman teknis (opsional):* mencocokkan *bounded context* hasil lokakarya dengan modul dan tabel basis data aplikasi yang ada.

**Latihan.**
1. Kata "pasien" bisa bermakna berbeda di bagian pendaftaran, keuangan, dan laboratorium. Jelaskan cara *bounded context* menangani perbedaan makna ini.
2. Tentukan apakah layanan penagihan di Medikara Health termasuk *core*, *supporting*, atau *generic subdomain*. Jelaskan konsekuensinya terhadap keputusan membangun sendiri atau membeli.
3. Mengapa integrasi dengan sistem eksternal seperti BPJS Kesehatan sebaiknya dilindungi oleh *anticorruption layer*?

#### Pertemuan 07 · Monolit, Modular Monolith, dan Microservices

**Tujuan.**
1. Membandingkan monolit, *modular monolith*, dan *microservices* dari sisi manfaat dan biayanya.
2. Mendiagnosis sumber keterkaitan (*coupling*) pada aplikasi yang ada.
3. Menuliskan keputusan gaya arsitektur dalam format ADR.

**Topik.** Monolit, *modular monolith*, dan *microservices*. *Coupling* dan *cohesion*. Biaya sistem terdistribusi dan *fallacies of distributed computing*. Hukum Conway: struktur komunikasi tim membentuk struktur sistem. Kapan *microservices* tidak tepat, termasuk pelajaran dari Segment yang kembali ke monolit. Pendekatan *monolith first*. Membaca kajian ilmiah tentang perjalanan *microservices* secara kritis. ADR (*Architecture Decision Record*) sebagai catatan keputusan.

**Aktivitas.** Tim mendiagnosis SIMRS atau aplikasi inti organisasi: bagian yang sering berubah bersamaan, bagian yang paling sering menimbulkan gangguan, dan tim yang mengelolanya. Anggota non-teknis mengumpulkan data dampak bisnis dan pola permintaan perubahan dari pengguna. Anggota teknis memetakan modul dan dependensinya. Tim menulis ADR pertama yang memilih satu gaya arsitektur target, lengkap dengan opsi yang ditolak dan konsekuensinya. Seluruh artefak C2 dirapikan untuk tinjauan menjelang UTS. Luarannya adalah diagnosis arsitektur aplikasi dan ADR gaya arsitektur untuk C2. *Pendalaman teknis (opsional):* mengukur keterkaitan antarmodul pada satu basis kode *open source* dengan alat analisis dependensi.

**Latihan.**
1. Sebuah tim berisi enam pengembang ingin memecah aplikasinya menjadi dua puluh *microservices*. Ajukan tiga pertanyaan yang perlu dijawab sebelum rencana itu disetujui.
2. Jelaskan mengapa *modular monolith* sering menjadi titik tengah yang masuk akal bagi organisasi seperti Medikara Health.
3. Baca kisah Segment yang kembali ke monolit. Apa penyebab utamanya, dan apakah penyebab itu juga ada di organisasi pilihan tim?

### Bagian III. Merancang Arsitektur Target (8 sampai 11)

#### Pertemuan 08 · Container, Kubernetes, dan Serverless

**Tujuan.**
1. Menjelaskan perbedaan *virtual machine*, *container*, dan *serverless* dengan analogi dan contoh.
2. Menjelaskan cara Kubernetes menjaga sistem tetap sesuai keadaan yang diinginkan.
3. Memilih *runtime* untuk setiap kandidat layanan berdasarkan kriteria yang eksplisit.

**Topik.** VM (*Virtual Machine*) dan *container*. *Container image* dan *registry*. Orkestrasi *container*. Konsep Kubernetes: *desired state*, *pod*, *deployment*, *service*, *self-healing*, dan *autoscaling*. *Managed* Kubernetes dibandingkan dengan PaaS. *Serverless* dan FaaS (*Function as a Service*): skala sampai nol, *cold start*, dan biaya per eksekusi. Kriteria memilih *runtime*. *Vendor lock-in* dan portabilitas. Kubernetes sebagai platform bersama untuk *workload* AI (*Artificial Intelligence*) menurut survei CNCF 2025.

**Aktivitas.** Tim mengambil kandidat layanan dari Pertemuan 6 dan 7, lalu memilih *runtime* untuk masing-masing: SaaS, PaaS, *managed* Kubernetes, *serverless*, atau tetap di VM. Kriteria keputusan ditetapkan lebih dulu, misalnya pola beban, kebutuhan latensi, keterampilan tim, biaya, dan aturan lokasi data dari Pertemuan 2. Anggota teknis menjelaskan konsekuensi operasional setiap opsi. Anggota non-teknis menilai biaya, ketersediaan tenaga kerja di pasar, dan risiko ketergantungan pada penyedia. Luarannya adalah matriks keputusan *runtime* per layanan untuk C3. *Pendalaman teknis (opsional):* membuat *container image* untuk aplikasi contoh, lalu menjalankannya pada klaster Kubernetes lokal dengan kind atau minikube.

**Latihan.**
1. Jelaskan kepada direktur keuangan mengapa layanan pengingat jadwal kontrol pasien cocok dijalankan secara *serverless*.
2. Kapan Kubernetes justru menjadi beban bagi organisasi? Berikan dua kondisi beserta alasannya.
3. Bandingkan risiko *vendor lock-in* pada layanan *serverless* dan pada *managed* Kubernetes.

#### Pertemuan 09 · Komunikasi Antarlayanan dan Event-Driven Architecture

**Tujuan.**
1. Membedakan komunikasi sinkron dan asinkron beserta dampaknya terhadap ketersediaan layanan.
2. Memodelkan proses bisnis sebagai rangkaian *event*.
3. Membandingkan koordinasi berbasis *choreography* dan *orchestration*.

**Topik.** Komunikasi sinkron dan asinkron. *Request/response*. Antrean pesan dan *publish/subscribe*. *Event broker*. Tiga pola *event*: *event notification*, *event-carried state transfer*, dan *event sourcing*. *Choreography* dan *orchestration*. Pengiriman *at-least-once* dan *consumer* yang idempoten. *Service mesh* pada tingkat konsep. Gaya API (*Application Programming Interface*), desain kontrak, dan *API gateway* disinggung singkat (dibahas rinci di IT40613).

**Aktivitas.** Tim memodelkan alur janji temu Medikara+ atau alur sejenis di organisasi pilihan: pasien membuat janji, jadwal dokter terkunci, pengingat terkirim, hasil laboratorium tersedia, dan tagihan terbit. Anggota non-teknis menuliskan kejadian bisnis dan pihak yang perlu mengetahuinya. Anggota teknis menentukan pola komunikasi untuk setiap interaksi beserta alasannya. Luarannya adalah peta interaksi layanan dan katalog *event* untuk C3. *Pendalaman teknis (opsional):* menjalankan RabbitMQ atau Apache Kafka secara lokal, lalu mengirim dan menerima satu *event* `JanjiTemuDibuat`.

**Latihan.**
1. Layanan notifikasi mati selama satu jam. Apa akibatnya pada alur janji temu yang memakai komunikasi sinkron, dan apa bedanya bila alur itu memakai *event*?
2. Jelaskan mengapa *consumer* harus idempoten ketika pesan dapat terkirim lebih dari sekali. Berikan contoh dari proses pembayaran.
3. Kapan *orchestration* lebih tepat daripada *choreography*? Gunakan contoh proses klaim asuransi.

#### Pertemuan 10 · Data dalam Microservices: Saga dan Outbox

**Tujuan.**
1. Menjelaskan alasan setiap layanan memiliki datanya sendiri dan risiko basis data bersama.
2. Merancang saga beserta langkah kompensasinya untuk satu proses lintas layanan.
3. Menjelaskan cara pola *transactional outbox* mencegah data dan *event* tidak sinkron.

**Topik.** *Database per service*. Basis data bersama sebagai *anti-pattern*. Masalah transaksi terdistribusi. *Eventual consistency*. Saga, dari gagasan asli Garcia-Molina dan Salem (1987) sampai penerapannya pada *microservices*. Saga berbasis *choreography* dan *orchestration*. Transaksi kompensasi. Pola *transactional outbox*. CQRS (*Command Query Responsibility Segregation*) dan *read model* untuk laporan manajemen. Kepemilikan data pasien dalam strategi "Satu Pasien, Satu Rekam Medis". Arsitektur data tingkat *enterprise* disinggung singkat (dibahas rinci di IT40513).

**Aktivitas.** Tim membuat peta kepemilikan data: entitas utama, layanan pemiliknya, dan layanan yang hanya membaca. Tim lalu merancang satu saga, misalnya pendaftaran pasien rujukan dari klinik mitra sampai klaim terkirim, lengkap dengan langkah kompensasi ketika salah satu langkah gagal. Anggota non-teknis memastikan aturan bisnis dan kompensasinya masuk akal bagi pasien dan bagian keuangan. Anggota teknis memilih pola koordinasi dan titik pemakaian *outbox*. Luarannya adalah peta kepemilikan data dan rancangan saga untuk C3. *Pendalaman teknis (opsional):* menerapkan *outbox* sederhana dengan PostgreSQL dan satu proses pembaca yang menerbitkan *event*.

**Latihan.**
1. Mengapa tim keuangan dan tim layanan pasien sebaiknya tidak menulis langsung ke tabel basis data yang sama?
2. Pada saga pendaftaran rujukan, verifikasi kepesertaan BPJS Kesehatan gagal setelah jadwal dokter dikunci. Uraikan langkah kompensasinya.
3. Laporan manajemen Medikara Health masih disusun dengan *spreadsheet*. Jelaskan cara *read model* menggantikan kebiasaan itu tanpa membebani layanan operasional.

#### Pertemuan 11 · Observability, SRE, dan SLO

**Tujuan.**
1. Membedakan *monitoring* dan *observability* serta tiga sinyal telemetri: *log*, metrik, dan *trace*.
2. Menetapkan SLI, SLO, dan *error budget* untuk perjalanan pengguna yang kritis.
3. Menjelaskan praktik SRE (*Site Reliability Engineering*) yang menyeimbangkan kecepatan perubahan dan keandalan.

**Topik.** *Monitoring* dan *observability*. *Log*, metrik, dan *trace*. OpenTelemetry sebagai standar terbuka instrumentasi. SLI, SLO, dan SLA (*Service Level Agreement*). *Error budget* dan kebijakannya. Praktik SRE: *toil*, *alerting* yang bermakna, penanganan insiden, dan *postmortem* tanpa menyalahkan. SLO berbasis perjalanan pengguna. KPI (*Key Performance Indicator*) dan pelaporan ke direksi disinggung singkat (dibahas rinci di IT40813).

**Aktivitas.** Tim memilih dua sampai tiga perjalanan pengguna yang paling kritis, misalnya membuat janji temu lewat Medikara+, mengambil hasil laboratorium, dan mengirim klaim BPJS Kesehatan. Anggota non-teknis menentukan arti "layanan yang baik" dari sisi pasien dan manajemen. Anggota teknis menerjemahkannya menjadi SLI yang terukur, target SLO, dan sinyal telemetri yang dibutuhkan. Tim menulis kebijakan *error budget* sepanjang satu halaman. Luarannya adalah SLO layanan kritis dan rancangan *observability* untuk C3. *Pendalaman teknis (opsional):* menginstrumentasi aplikasi contoh dengan OpenTelemetry, lalu menampilkan satu *trace* yang melintasi dua layanan.

**Latihan.**
1. Hitung waktu tidak tersedia yang diizinkan dalam satu bulan untuk SLO ketersediaan 99,5 persen dan 99,9 persen. Jelaskan dampak selisihnya bagi biaya.
2. Mengapa target SLO 100 persen hampir selalu merupakan keputusan yang buruk?
3. Usulkan satu SLI untuk layanan janji temu yang mencerminkan pengalaman pasien, bukan sekadar kondisi *server*.

### Bagian IV. Operasi, Peta Jalan, dan Tata Kelola (12 sampai 14)

#### Pertemuan 12 · Resiliensi dan Disaster Recovery

**Tujuan.**
1. Mengidentifikasi mode kegagalan dalam sistem terdistribusi dan pola resiliensi untuk menanganinya.
2. Menetapkan RTO dan RPO berdasarkan dampak bisnis.
3. Memilih strategi DR yang seimbang antara biaya dan risiko.

**Topik.** Mode kegagalan dalam sistem terdistribusi. Pola resiliensi: *timeout*, *retry* dengan *backoff*, *circuit breaker*, *bulkhead*, dan *graceful degradation*. Penerapan *multi-AZ* dan *multi-region*. RTO (*Recovery Time Objective*) dan RPO (*Recovery Point Objective*). Strategi DR (*Disaster Recovery*): *backup and restore*, *pilot light*, *warm standby*, dan *multi-site active-active*. Cadangan yang tidak dapat diubah sebagai pertahanan terhadap *ransomware*. Pelajaran dari insiden PDNS 2 (Pusat Data Nasional Sementara 2) Surabaya pada 2024. *Chaos engineering* dan *game day*. Kelangsungan bisnis dan ISO 22301 disinggung singkat (dibahas rinci di IT40813).

**Aktivitas.** Tim menetapkan RTO dan RPO untuk layanan kritis dari Pertemuan 11, memilih strategi DR untuk masing-masing, lalu memperkirakan biaya tambahannya. Anggota non-teknis memimpin analisis dampak bisnis: kerugian per jam, dampak pada keselamatan pasien, dan kewajiban regulasi. Anggota teknis memetakan pola resiliensi dan arsitektur DR. Tim menyusun satu skenario uji pemulihan, misalnya region utama tidak tersedia selama empat jam. Luarannya adalah rencana resiliensi dan DR beserta jadwal uji pemulihan untuk C4. *Pendalaman teknis (opsional):* mensimulasikan kegagalan satu layanan dan mengamati perilaku *circuit breaker* dengan pustaka resiliensi.

**Latihan.**
1. Jelaskan perbedaan RTO dan RPO dengan contoh layanan rekam medis elektronik.
2. Pada insiden PDNS 2 tahun 2024, hanya sebagian kecil data yang memiliki cadangan. Pelajaran arsitektur dan tata kelola apa yang dapat diambil?
3. Mengapa strategi *multi-site active-active* belum tentu tepat untuk semua layanan Medikara Health?

#### Pertemuan 13 · DevOps, GitOps, dan Platform Engineering

**Tujuan.**
1. Menjelaskan praktik DevOps dan metrik DORA (DevOps Research and Assessment) untuk mengukur kinerja pengiriman perangkat lunak.
2. Menjelaskan alur CI/CD (*Continuous Integration / Continuous Delivery*) dan empat prinsip GitOps.
3. Merancang topologi tim dan peran platform internal bagi organisasi.

**Topik.** Budaya dan praktik DevOps. Metrik DORA: frekuensi *deployment*, *lead time* perubahan, tingkat kegagalan perubahan, dan waktu pemulihan. Temuan laporan DORA 2025 bahwa AI memperkuat kondisi organisasi, baik kekuatan maupun kelemahannya. Alur CI/CD. Strategi rilis *blue-green* dan *canary*. IaC (*Infrastructure as Code*). Empat prinsip OpenGitOps. *Platform engineering* dan IDP (*Internal Developer Platform*): *golden path*, *self-service*, dan *platform as a product* menurut CNCF Platforms White Paper. Team Topologies: empat tipe tim dan tiga mode interaksi. Keamanan rantai pasok perangkat lunak disinggung singkat (dibahas rinci di IT40813).

**Aktivitas.** Tim memetakan alur perubahan saat ini, dari permintaan fitur sampai berjalan di produksi, lalu menandai antrean dan langkah manual. Anggota non-teknis memimpin pemetaan waktu tunggu dan rantai persetujuan. Anggota teknis merancang alur CI/CD dan GitOps target. Tim lalu menyusun topologi tim target, yaitu tim *stream-aligned*, tim platform, dan tim *enabling*, beserta tiga sampai lima kapabilitas platform internal yang diprioritaskan. Luarannya adalah model operasi *delivery* dan peta jalan platform internal untuk C4. *Pendalaman teknis (opsional):* membuat *pipeline* CI sederhana dengan GitHub Actions, lalu menyinkronkan *manifest* Kubernetes dengan Argo CD atau Flux.

**Latihan.**
1. Organisasi yang merilis perubahan setiap tiga bulan sering menganggap rilis yang jarang lebih aman. Kritisi anggapan ini dengan merujuk temuan DORA.
2. Apa perbedaan tim platform dengan divisi infrastruktur tradisional yang melayani tiket?
3. Jelaskan cara GitOps membantu auditor menelusuri siapa mengubah apa di lingkungan produksi.

#### Pertemuan 14 · Peta Jalan Modernisasi dan Tata Kelola Cloud

**Tujuan.**
1. Menyusun urutan modernisasi bertahap dengan pola *strangler fig*.
2. Merancang *guardrail* tata kelola *cloud* untuk biaya, keamanan, dan lokasi data.
3. Mempertahankan peta jalan modernisasi di depan pemangku kepentingan dengan metrik yang terukur.

**Topik.** Pola *strangler fig* dan modernisasi bertahap. *Anticorruption layer* selama masa transisi. Penyusunan gelombang modernisasi berdasarkan dependensi, risiko, dan nilai. *Guardrail* dan *policy as code* pada *landing zone*. FinOps pada fase Operate: anggaran, deteksi anomali, dan kebijakan *tagging*. Kedaulatan data dan pilihan *sovereign cloud*. Metrik peta jalan: metrik DORA, SLO, biaya per unit, dan jejak karbon. Teknik penyusunan peta jalan dan perencanaan migrasi tingkat *enterprise* disinggung singkat (dibahas rinci di IT40513).

**Aktivitas.** Tim menyatukan artefak Pertemuan 1 sampai 13 menjadi peta jalan modernisasi tiga gelombang. Setiap gelombang memuat layanan yang dimodernisasi, strategi 7R, prasyarat platform, sasaran SLO dan biaya, serta risikonya. Anggota non-teknis memimpin narasi nilai bisnis dan urutan prioritas. Anggota teknis memeriksa kelayakan dependensi dan prasyarat teknis. Tim juga menetapkan lima sampai tujuh *guardrail* tata kelola, misalnya "data rekam medis hanya boleh disimpan di region yang berlokasi di Indonesia". Hasilnya dipresentasikan sebagai bagian C4 menjelang UAS. Luarannya adalah peta jalan modernisasi dan *guardrail* tata kelola *cloud* untuk C4. *Pendalaman teknis (opsional):* menulis satu kebijakan *policy as code* dengan Open Policy Agent yang menolak sumber daya di luar region yang diizinkan.

**Latihan.**
1. Jelaskan mengapa pola *strangler fig* lebih aman daripada mengganti SIMRS sekaligus dalam satu kali peralihan.
2. Susun tiga *guardrail* tata kelola *cloud* untuk Medikara Health dan jelaskan risiko yang dicegah oleh masing-masing.
3. Pilih empat metrik untuk melaporkan kemajuan peta jalan kepada direksi. Jelaskan mengapa metrik tersebut lebih bermakna daripada jumlah aplikasi yang sudah dipindahkan.

---

## Kaitan dengan Capstone

| Tonggak | Pertemuan | Luaran dari mata kuliah ini |
| --- | --- | --- |
| C1 Konteks dan Strategi | 1 sampai 3 | Profil organisasi dan daftar pemicu modernisasi. Matriks kendala penempatan *workload*, termasuk aturan lokasi data. Model biaya awal berupa TCO kasar, metrik biaya per unit, dan sasaran nilai *cloud*. |
| C2 Kondisi Saat Ini | 4 sampai 7 | Penilaian kesiapan *cloud* dengan enam perspektif CAF. Portofolio aplikasi dengan usulan 7R. Kartu skor kesenjangan *cloud-native*. Peta domain dan *context map* kondisi saat ini. Diagnosis arsitektur aplikasi inti dan ADR gaya arsitektur. Ditinjau menjelang UTS. |
| C3 Kondisi Target | 8 sampai 11 | Matriks keputusan *runtime* per layanan. Peta interaksi layanan dan katalog *event*. Peta kepemilikan data dan rancangan saga. SLO layanan kritis dan rancangan *observability*. |
| C4 Peta Jalan dan Tata Kelola | 12 sampai 14 | Rencana resiliensi dan DR beserta jadwal uji pemulihan. Model operasi *delivery* dan peta jalan platform internal. Peta jalan modernisasi tiga gelombang dan *guardrail* tata kelola *cloud*. Dipresentasikan menjelang UAS. |

Artefak mata kuliah ini saling mengisi dengan artefak tiga mata kuliah lain. *Capability map* dan arsitektur aplikasi dari IT40513 menjadi masukan lokakarya EventStorming pada Pertemuan 6. Portofolio API dari IT40613 menjadi masukan peta interaksi layanan pada Pertemuan 9. Risiko yang muncul dari matriks lokasi data (Pertemuan 2) dan rencana DR (Pertemuan 12) masuk ke *risk register* dan rencana kelangsungan bisnis di IT40813. Peta jalan modernisasi pada Pertemuan 14 menjadi bagian teknis dari peta jalan *enterprise* yang disusun di IT40513.

## Kasus Berjalan: Medikara Health

PT Medikara Nusa Sehat, disingkat Medikara Health, adalah organisasi **fiktif** yang dipakai bersama oleh keempat mata kuliah. Seluruh angka dan kejadian di dalamnya rekaan. Medikara Health adalah jaringan layanan kesehatan swasta dengan 5 rumah sakit (Jakarta, Bekasi, Depok, Bogor, dan Bandung), 18 klinik pratama, 1 laboratorium rujukan, dan 12 apotek. Karyawannya sekitar 4.800 orang, dengan sekitar 1,2 juta kunjungan pasien per tahun.

**Kondisi saat ini.** Setiap rumah sakit menjalankan SIMRS (Sistem Informasi Manajemen Rumah Sakit) monolitik *on-premise* dengan versi berbeda karena berasal dari akuisisi. ERP (*Enterprise Resource Planning*) keuangan sudah terpusat. Aplikasi pasien Medikara+ untuk janji temu dan telekonsultasi dibuat oleh vendor. Integrasi ke BPJS Kesehatan dan ke SATUSEHAT milik Kementerian Kesehatan, yang berbasis HL7 FHIR (*Health Level Seven Fast Healthcare Interoperability Resources*), dibangun secara *point-to-point*. Data pasien tersebar, dan banyak laporan manajemen masih disusun dengan *spreadsheet*.

**Strategi 2026 sampai 2030.** Strategi berjudul "Satu Pasien, Satu Rekam Medis" menargetkan layanan terintegrasi lintas fasilitas, ekosistem mitra yang terbuka (klinik mitra, asuransi, laboratorium, apotek daring, dan layanan kesehatan karyawan perusahaan), modernisasi ke *cloud*, serta kepatuhan pada UU PDP dan aturan rekam medis elektronik.

**Pemicu tambahan.** Insiden kebocoran data pasien skala kecil lewat vendor pada 2025. Temuan audit internal tentang kontrol akses yang lemah. Antrean layanan yang panjang. Biaya integrasi yang tinggi.

**Pemakaian dalam mata kuliah ini.** Kasus dipakai sebagai contoh di setiap bab dan sebagai pengganti bagi tim yang tidak punya akses ke organisasi nyata.

- Pertemuan 1 sampai 3: pemicu modernisasi, kendala lokasi data rekam medis dan data pribadi, serta perkiraan biaya infrastruktur per kunjungan pasien.
- Pertemuan 4 sampai 7: portofolio aplikasi hasil akuisisi, SIMRS berbeda versi sebagai bahan penilaian 7R dan *twelve-factor*, lokakarya EventStorming dari pendaftaran sampai klaim BPJS Kesehatan, dan diagnosis keterkaitan SIMRS.
- Pertemuan 8 sampai 11: pilihan *runtime* untuk Medikara+ dan layanan pendukungnya, alur janji temu berbasis *event*, saga pendaftaran pasien rujukan dari klinik mitra, *read model* pengganti laporan *spreadsheet*, dan SLO untuk perjalanan pasien.
- Pertemuan 12 sampai 14: rencana DR untuk rekam medis elektronik, model operasi tim TI setelah akuisisi, dan peta jalan modernisasi menuju "Satu Pasien, Satu Rekam Medis".

## Struktur Repositori

- `figures/`: gambar untuk modul dan slide. `figures/logo_universitas.png` dan `figures/building.png` adalah symlink.
- `module/`: naskah modul LaTeX. Berkas utama `cloud-native-microservices-architecture.tex` memuat `titlepage.tex` dan `chapter01.tex` sampai `chapter14.tex`. Rujukan inti ada di `references.bib`, sedangkan rujukan khusus satu bab ada di `bib/chapterNN.bib`. Folder `module/fonts` adalah symlink.
- `slides/`: slide per pertemuan di `slides/sessionNN/`, memakai `slides/preamble.tex` bersama. Folder `slides/theme` adalah symlink.
- `sources/`: berkas pendukung per bab di `sources/chapterNN/`, misalnya lembar kerja, templat, data kasus, dan berkas teknis opsional yang dirujuk dari naskah modul.

Modul dan slide dikompilasi dengan XeLaTeX. Modul dikompilasi di folder `module`:

```bash
cd module
xelatex cloud-native-microservices-architecture
bibtex cloud-native-microservices-architecture
xelatex cloud-native-microservices-architecture
xelatex cloud-native-microservices-architecture
```

Slide dikompilasi di folder setiap pertemuan, misalnya `slides/session01`:

```bash
cd slides/session01
xelatex session01
xelatex session01
```

`module/fonts`, `slides/theme`, `figures/logo_universitas.png`, dan `figures/building.png` adalah symlink ke repo advanced-software-engineering (target `/data2/projects/advanced-software-engineering/...`). Pada mesin yang tidak memiliki repo tersebut di lokasi itu, atau pada Windows yang tidak mengaktifkan symlink, keempat aset tersebut perlu disalin dari repo advanced-software-engineering sebelum kompilasi.

## Rujukan Utama

Versi dan status di bawah ini diperiksa pada 30 Oktober 2026.

**Definisi, prinsip, dan buku inti**

- CNCF TOC. *Cloud Native Definition* v1.1, disetujui 26 Februari 2024. <https://github.com/cncf/toc/blob/main/DEFINITION.md>
- Mell, P. dan Grance, T. *The NIST Definition of Cloud Computing*, NIST SP 800-145, 2011. Masih berstatus final dan belum direvisi. <https://doi.org/10.6028/NIST.SP.800-145>
- Wiggins, A. dkk. *The Twelve-Factor App*. Dibuka sebagai proyek *open source* sejak 12 November 2024 dan kini diperbarui oleh komunitas. <https://12factor.net/>
- Lewis, J. dan Fowler, M. *Microservices*, 2014. <https://martinfowler.com/articles/microservices.html>
- Newman, S. *Building Microservices*, edisi ke-2. O'Reilly, 2021.
- Richardson, C. *Microservices Patterns*. Manning, 2018. Edisi ke-2 masih dalam MEAP (*Manning Early Access Program*) dengan perkiraan terbit 2027. <https://microservices.io/patterns/>
- Evans, E. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003.
- Vernon, V. *Implementing Domain-Driven Design*. Addison-Wesley, 2013.
- Richards, M. dan Ford, N. *Fundamentals of Software Architecture*, edisi ke-2. O'Reilly, 2025.
- Skelton, M. dan Pais, M. *Team Topologies*, edisi ke-2. IT Revolution, 2025.
- Storment, J.R. dan Fuller, M. *Cloud FinOps*, edisi ke-2. O'Reilly, 2023.
- Beyer, B., Jones, C., Petoff, J., dan Murphy, N.R. (ed.). *Site Reliability Engineering*. O'Reilly, 2016. <https://sre.google/sre-book/table-of-contents/>

**Kerangka penyedia dan komunitas**

- AWS. *An Overview of the AWS Cloud Adoption Framework*, 2021. <https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html>
- AWS Prescriptive Guidance. *About the migration strategies* (7R). <https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html>
- AWS. *AWS Well-Architected Framework*, enam pilar. <https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html>
- Microsoft. *Cloud Adoption Framework for Azure*, pembaruan Agustus 2026 dengan tujuh fase dan skenario *sovereignty*. <https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview>
- Google Cloud. *The Google Cloud Adoption Framework*, 2018. <https://services.google.com/fh/files/misc/google_cloud_adoption_framework_whitepaper.pdf>
- Google Cloud. *Well-Architected Framework*, enam pilar, diperbarui 13 Oktober 2026. <https://docs.cloud.google.com/architecture/framework>
- FinOps Foundation. *FinOps Framework* 2026, dengan *capability* baru Executive Strategy Alignment. <https://www.finops.org/framework/>
- FinOps Foundation. *FOCUS Specification* 1.4, diratifikasi 4 Juni 2026. <https://focus.finops.org/focus-specification/>
- CNCF TAG App Delivery. *CNCF Platforms White Paper* v1.0 dan *Platform Engineering Maturity Model* v1.0. <https://tag-app-delivery.cncf.io/whitepapers/platforms/> dan <https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/>
- OpenGitOps. *GitOps Principles* v1.0.0. <https://opengitops.dev/>
- OpenTelemetry. *What is OpenTelemetry?* <https://opentelemetry.io/docs/what-is-opentelemetry/>
- ISO/IEC 21031:2024. *Information technology: Software Carbon Intensity (SCI) specification*. <https://www.iso.org/standard/86612.html>

**Laporan industri dan artikel**

- DORA. *State of AI-assisted Software Development* 2025. <https://dora.dev/research/2025/dora-report/>
- CNCF. *The CNCF Annual Cloud Native Survey* (survei 2025, terbit 20 Januari 2026). <https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/>
- Flexera. *2026 State of the Cloud Report*. <https://info.flexera.com/CM-REPORT-State-of-the-Cloud>
- Jamshidi, P. dkk. "Microservices: The Journey So Far and Challenges Ahead". *IEEE Software* 35(3), 2018. <https://doi.org/10.1109/MS.2018.2141039>
- Garcia-Molina, H. dan Salem, K. "Sagas". *Proceedings of ACM SIGMOD*, 1987. <https://doi.org/10.1145/38713.38742>
- Noonan, A. "Goodbye Microservices: From 100s of problem children to 1 superstar". Segment Engineering, 2018. <https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices>

**Regulasi dan konteks Indonesia**

- PP 71/2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik. Berlaku. Pasal 20 dan 21 mengatur lokasi pengelolaan data untuk lingkup publik dan privat. Rencana revisinya masih dalam tahap evaluasi Kementerian Komunikasi dan Digital (Komdigi). <https://peraturan.bpk.go.id/Details/122030/pp-no-71-tahun-2019>
- Permenkominfo 5/2020 tentang Penyelenggara Sistem Elektronik Lingkup Privat, diubah dengan Permenkominfo 10/2021. Berlaku. <https://peraturan.bpk.go.id/Details/203049>
- Permenkes 24/2022 tentang Rekam Medis. Berlaku. Pasal 20 mengizinkan penyimpanan rekam medis elektronik di *server*, *cloud computing* yang tersertifikasi, atau media digital lain. <https://peraturan.bpk.go.id/Details/245544>
- UU 27/2022 tentang Pelindungan Data Pribadi. Berlaku. <https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022>
- PP 33/2026 sebagai aturan pelaksana UU PDP, ditetapkan 16 Juli 2026 dan berlaku 16 Januari 2027 menurut ringkasan firma hukum. Teks resminya perlu dicek ulang di JDIH (Jaringan Dokumentasi dan Informasi Hukum) sebelum dikutip. <https://www.allenandgledhill.com/perspectives/publications/knowledge-updates-indonesia/2026/indonesia-data-protection-regulation-33-introduces-new-operational-requirements/>
- Region *cloud* di Indonesia: AWS Asia Pacific (Jakarta) sejak Desember 2021 <https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-jakarta-region/>, Google Cloud Jakarta sejak Juni 2020 <https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-jakarta-now-open>, Microsoft Azure Indonesia Central sejak 2025 <https://news.microsoft.com/id-id/2025/05/27/microsoft-opens-indonesia-central/>, dan Oracle Cloud Indonesia North (Batam) sejak 2025 <https://docs.oracle.com/iaas/releasenotes/oci/new-region-batam.htm>.
- Insiden PDNS 2 Surabaya 2024 sebagai kasus pemulihan bencana. <https://teknologi.bisnis.com/read/20240923/101/1801625/pdns-2-gangguan-3-bulan-proses-pemulihan-capai-73>

**Silabus pembanding**

- Johns Hopkins University, Engineering for Professionals. EN.605.702 *Cloud-native Architecture and Microservices*. <https://ep.jhu.edu/courses/605702-cloud-native-architecture-and-microservices>
- University of Chicago, Masters Program in Computer Science. MPCS 51205 *Topics in Software Engineering* (*microservices*, DDD, dan *event-driven architecture*). <https://classes.cs.uchicago.edu/archive/2022/fall/51205-1/syllabus.html>
- National University of Singapore, NUS-ISS. *Graduate Certificate in Architecting Scalable Systems*, termasuk kursus *Cloud Native Solution Design*. <https://www.iss.nus.edu.sg/stackable-certificate-programmes/software-engineering/graduate-certificate-in-architecting-scalable-systems>

## Daftar Singkatan

| Singkatan | Kepanjangan |
| --- | --- |
| ADR | Architecture Decision Record |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| AWS | Amazon Web Services |
| AZ | Availability Zone |
| BPJS | Badan Penyelenggara Jaminan Sosial |
| CAF | Cloud Adoption Framework |
| CapEx | Capital Expenditure |
| CCoE | Cloud Center of Excellence |
| CI/CD | Continuous Integration / Continuous Delivery |
| CNCF | Cloud Native Computing Foundation |
| CQRS | Command Query Responsibility Segregation |
| CS | Computer Science |
| DDD | Domain-Driven Design |
| DORA | DevOps Research and Assessment |
| DR | Disaster Recovery |
| ERP | Enterprise Resource Planning |
| FaaS | Function as a Service |
| FHIR | Fast Healthcare Interoperability Resources |
| FOCUS | FinOps Open Cost and Usage Specification |
| HL7 | Health Level Seven |
| IaaS | Infrastructure as a Service |
| IaC | Infrastructure as Code |
| IDP | Internal Developer Platform |
| JDIH | Jaringan Dokumentasi dan Informasi Hukum |
| Komdigi | Kementerian Komunikasi dan Digital |
| KPI | Key Performance Indicator |
| MEAP | Manning Early Access Program |
| NIST | National Institute of Standards and Technology |
| OpEx | Operational Expenditure |
| PaaS | Platform as a Service |
| PDNS | Pusat Data Nasional Sementara |
| PDP | Pelindungan Data Pribadi |
| Permenkes | Peraturan Menteri Kesehatan |
| Permenkominfo | Peraturan Menteri Komunikasi dan Informatika |
| PP | Peraturan Pemerintah |
| PSE | Penyelenggara Sistem Elektronik |
| PSTE | Penyelenggaraan Sistem dan Transaksi Elektronik |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SaaS | Software as a Service |
| SCI | Software Carbon Intensity |
| SE | Software Engineering |
| SIMRS | Sistem Informasi Manajemen Rumah Sakit |
| SLA | Service Level Agreement |
| SLI | Service Level Indicator |
| SLO | Service Level Objective |
| SRE | Site Reliability Engineering |
| TCO | Total Cost of Ownership |
| TI | Teknologi Informasi |
| UAS | Ujian Akhir Semester |
| UTS | Ujian Tengah Semester |
| UU | Undang-Undang |
| VM | Virtual Machine |
