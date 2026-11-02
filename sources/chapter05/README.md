# Sumber Bab 05

Berkas pendukung Aktivitas dan Latihan Bab 05, Prinsip Cloud-Native dan
Twelve-Factor App. Semua angka dan nilai konfigurasi di dalamnya rekaan untuk
kasus fiktif Medikara Health.

| Berkas | Kegunaan |
| --- | --- |
| `kartu-skor-twelve-factor.xlsx` | Kartu skor kesenjangan *cloud-native* untuk 2 sampai 3 aplikasi inti. Lembar Petunjuk, Kartu Skor (isian), Contoh Medikara (sama dengan tabel contoh kartu skor di seksi Aktivitas), dan Tiga Kesenjangan. Luaran Aktivitas untuk tonggak C2. |
| `pertanyaan-bukti-per-faktor.md` | Pertanyaan berbahasa sehari-hari dan bukti yang dicari untuk setiap faktor, beserta tanda skor 3 dan skor 0. Dibawa ke wawancara dengan tim TI atau vendor. |
| `contoh-aplikasi-konfigurasi/app.py` | Aplikasi contoh Python (pustaka standar saja) untuk pendalaman teknis: konfigurasi dari *environment variable*, *log* JSON ke `stdout`, proses tanpa *state*, dan berhenti rapi saat `SIGTERM`. Sumber Listing konfigurasi dan *log* di naskah. |
| `contoh-aplikasi-konfigurasi/contoh-bogor.env` | Contoh nilai konfigurasi RS Bogor untuk `app.py`. Nilai rekaan; kunci asli tidak boleh ditulis di berkas teks. |
| `contoh-aplikasi-konfigurasi/deployment.yaml` | Contoh manifest Kubernetes deklaratif untuk `app.py`, dirujuk dari seksi konfigurasi deklaratif di naskah. Hanya untuk dibaca; penerapannya dibahas pada Bab 8 dan Bab 13. |

## Menjalankan aplikasi contoh (opsional)

Jalankan hanya di komputer sendiri. Aplikasi ini tidak boleh diarahkan ke sistem
milik organisasi.

PowerShell:

```powershell
cd sources/chapter05/contoh-aplikasi-konfigurasi
$env:KODE_RUMAH_SAKIT = "RS-BOGOR"
$env:ALAMAT_BASIS_DATA = "postgresql://simrs-bogor.internal.example:5432/jadwal"
$env:KUNCI_AKSES_BPJS = "ganti-dengan-kunci-dari-pengelola-rahasia"
$env:PORT = "8080"
python app.py
```

Bash:

```bash
cd sources/chapter05/contoh-aplikasi-konfigurasi
set -a; . ./contoh-bogor.env; set +a
python3 app.py
```

Buka `http://localhost:8080/jadwal` di peramban. Setiap permintaan menulis satu
baris JSON ke terminal. Ulangi dengan `KODE_RUMAH_SAKIT=RS-BANDUNG` tanpa mengubah
kode untuk melihat faktor III bekerja. Di Linux atau macOS, hentikan proses dengan
`kill -TERM <pid>` untuk melihat *log* `proses_berhenti`. Bila salah satu variabel
wajib dikosongkan, aplikasi menolak menyala dan menulis *log*
`konfigurasi_tidak_lengkap`.
