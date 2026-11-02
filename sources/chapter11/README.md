<!-- Daftar berkas pendukung Bab 11 (Observability, SRE, dan SLO) beserta cara memakainya. -->

# Berkas Pendukung Bab 11: Observability, SRE, dan SLO

Berkas di folder ini dipakai untuk Aktivitas "SLO Layanan Kritis dan Rancangan Observability"
dan untuk Latihan Bab 11.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-slo.md` | Templat tabel perjalanan pengguna kritis, SLI, SLO, error budget, kebutuhan telemetri, dan alert. Dipakai pada langkah 1 sampai 4 Aktivitas. |
| `templat-kebijakan-error-budget.md` | Templat kebijakan error budget satu halaman: zona, tindakan, syarat postmortem, pengecualian, dan persetujuan. Dipakai pada langkah 5 Aktivitas. |
| `hitung_error_budget.py` | Kalkulator error budget dalam menit dan jumlah permintaan, serta laju pembakaran. Dipakai pada langkah 3 Aktivitas dan Latihan 1. |
| `contoh-opentelemetry/dua_layanan.py` | Contoh satu trace lintas dua layanan dengan OpenTelemetry, tanpa jaringan dan tanpa data pasien. Dipakai pada pendalaman teknis. |
| `contoh-opentelemetry/requirements.txt` | Daftar pustaka Python untuk `dua_layanan.py`. |

## Cara memakai

Kalkulator hanya membutuhkan Python 3:

```bash
python hitung_error_budget.py --target 99.5 99.9 --volume 28000
python hitung_error_budget.py --target 99.5 --gagal 9 --total 125
```

Contoh OpenTelemetry membutuhkan pustaka `opentelemetry-sdk`:

```bash
cd contoh-opentelemetry
python -m venv .venv
.venv/bin/pip install -r requirements.txt        # Windows: .venv\Scripts\pip
.venv/bin/python dua_layanan.py                  # Windows: .venv\Scripts\python
```

Keluarannya berisi header `traceparent` dan tiga span dalam format JSON. Ketiga span memiliki
`trace_id` yang sama, dan `parent_id` span "cek kuota poli" sama dengan `span_id` span
"panggil jadwal dokter".

## Etika

- Instrumentasi dan uji beban hanya untuk sistem milik tim sendiri atau sistem yang sudah
  memberi izin tertulis.
- Data organisasi nyata dipakai seizin organisasi dan dianonimkan. Telemetri tidak boleh memuat
  data pribadi pasien atau karyawan.
