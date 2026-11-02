<!-- Templat presentasi tonggak C4 untuk Aktivitas Bab 14. Salin berkas ini, isi setiap bagian bertanda "...", lalu pindahkan ke slide tim: 15 menit presentasi dan 10 menit tanya jawab. -->

# Templat Presentasi C4: Peta Jalan dan Tata Kelola

Durasi 15 menit presentasi dan 10 menit tanya jawab. Dosen dan tim lain berperan sebagai direksi.
Angka di slide wajib sama dengan angka di artefak C1 sampai C3.

| Menit | Bagian | Isi | Penyaji |
| :-- | :-- | :-- | :-- |
| 1 | Pertanyaan direksi | Apa yang dimodernisasi lebih dulu, berapa biayanya, bagaimana risikonya dikendalikan | Anggota non-teknis |
| 2 | Rekap keputusan | Tabel keputusan dari C1 sampai C3 dan dua artefak C4 lain; keputusan yang bertentangan dan penyelesaiannya | Penjaga konsistensi |
| 3 | Irisan pertama | Alasan pemilihan dengan lima kriteria; urutan pemindahan dengan *strangler fig* | Anggota teknis |
| 3 | Tiga gelombang | Isi, strategi 7R, prasyarat platform dan tim, sasaran SLO dan biaya, risiko, gerbang keputusan | Anggota non-teknis dan teknis |
| 3 | *Guardrail* | Lima sampai tujuh *guardrail*, jenis kendali, pemilik, jalur pengecualian | Perancang *guardrail* |
| 2 | Metrik kemajuan | Empat metrik dengan nilai awal dan sasaran per gerbang | Anggota non-teknis |
| 1 | Keputusan yang diminta | Satu sampai tiga keputusan konkret dari direksi | Seluruh anggota |

## Isian Slide

1. Organisasi dan pemicu modernisasi: ...
2. Keputusan yang dibawa dari artefak sebelumnya: ...
3. Irisan pertama dan alasannya: ...
4. Gelombang 1 (periode, isi, prasyarat, sasaran, risiko): ...
5. Gelombang 2 (periode, isi, prasyarat, sasaran, risiko): ...
6. Gelombang 3 (periode, isi, prasyarat, sasaran, risiko): ...
7. Kriteria gerbang keputusan: ...
8. Katalog *guardrail*: ...
9. Kedaulatan data dan status regulasi yang berlaku: ...
10. Kartu metrik: ...
11. Tiga risiko teratas: ...
12. Keputusan yang diminta dari direksi: ...

## Pertanyaan Latihan Tanya Jawab

Tim berlatih menjawab pertanyaan berikut dengan angka dari artefak sendiri.

- Mengapa tidak diganti sekaligus saja?
- Berapa biaya total sampai gerbang keputusan pertama, dan apa yang didapat bila berhenti di sana?
- Apa yang terjadi bila irisan pertama gagal, dan berapa lama kembali ke sistem lama?
- Mengapa jumlah aplikasi yang sudah dipindahkan tidak dilaporkan sebagai metrik utama?
- *Guardrail* mana yang paling mungkin menghambat tim, dan apa jalur pengecualiannya?
- Siapa yang dapat mengakses data pasien di *cloud*, dan bagaimana aksesnya dibuktikan?
- Regulasi mana yang masih bergerak, dan bagaimana peta jalan menyesuaikan diri?

## Daftar Periksa

- [ ] Setiap angka di slide dapat ditelusuri ke artefak sumbernya.
- [ ] Setiap gelombang punya prasyarat platform dan tim.
- [ ] Setiap gerbang keputusan punya kriteria yang dapat dibuktikan.
- [ ] Anggota non-teknis dan teknis sama-sama menyajikan.
- [ ] Data organisasi nyata dipakai seizin organisasi dan dianonimkan; tidak ada data pribadi pasien atau karyawan.
