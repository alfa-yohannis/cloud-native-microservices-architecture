# Contoh satu trace lintas dua layanan dengan OpenTelemetry, tanpa jaringan. Pakai:
# pip install -r requirements.txt, lalu jalankan: python dua_layanan.py
"""Menunjukkan cara satu trace melintasi layanan janji temu dan layanan jadwal dokter.

Kedua layanan disimulasikan dalam satu proses agar contoh dapat dijalankan di laptop
tanpa server atau penyimpanan telemetri. Yang dikirim antarlayanan hanya kamus header,
persis seperti header permintaan sungguhan. Akibatnya, mekanisme propagasi traceparent
terlihat jelas: kedua layanan mencetak span dengan trace_id yang sama.

Contoh ini tidak memakai data pasien. Atribut yang dicatat hanya kode poliklinik.
"""
import time

from opentelemetry import trace
from opentelemetry.propagate import extract, inject
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Lama kerja tiruan dalam detik. Dibuat kecil agar contoh cepat selesai, tetapi cukup
# besar agar durasi span terlihat berbeda di keluaran.
LAMA_CEK_KUOTA_DETIK = 0.3
LAMA_KUNCI_SLOT_DETIK = 0.1

# Kode poliklinik contoh. Bukan data pasien, sehingga aman dicetak.
KODE_POLI_CONTOH = "BDG-ANAK"


def buat_tracer(nama_layanan):
  """Membuat tracer yang memakai nama layanan sendiri.

  Setiap layanan sungguhan berjalan di proses terpisah dengan TracerProvider sendiri.
  Nama layanan dipasang sebagai resource agar penyimpanan telemetri dapat
  mengelompokkan span per layanan. SimpleSpanProcessor mencetak span begitu selesai;
  di produksi BatchSpanProcessor lebih hemat karena mengirim span berkelompok.
  """
  provider = TracerProvider(resource=Resource.create({"service.name": nama_layanan}))
  provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
  return provider.get_tracer(nama_layanan)


TRACER_JANJI_TEMU = buat_tracer("layanan-janji-temu")
TRACER_JADWAL_DOKTER = buat_tracer("layanan-jadwal-dokter")


# Tanpa extract, span di layanan ini menjadi trace baru yang terputus dari
# permintaan pasien, sehingga penelusuran lintas layanan gagal.
def layanan_jadwal_dokter(header_masuk, kode_poli):
  """Menjawab cek kuota; extract menyambung trace dari traceparent."""
  konteks_induk = extract(header_masuk)
  with TRACER_JADWAL_DOKTER.start_as_current_span(
    "cek kuota poli",
    context=konteks_induk,
    kind=trace.SpanKind.SERVER,
  ) as span:
    span.set_attribute("medikara.kode_poli", kode_poli)
    time.sleep(LAMA_CEK_KUOTA_DETIK)
    return True


# inject membuat layanan berikutnya tahu permintaan ini bagian dari trace yang
# mana, sehingga span-nya tersambung ke span pemanggil.
def layanan_janji_temu(kode_poli):
  """Memesan slot; inject menulis traceparent ke header keluar."""
  with TRACER_JANJI_TEMU.start_as_current_span(
    "pesan janji temu", kind=trace.SpanKind.SERVER
  ):
    with TRACER_JANJI_TEMU.start_as_current_span(
      "panggil jadwal dokter", kind=trace.SpanKind.CLIENT
    ):
      header_keluar = {}
      inject(header_keluar)
      print("Header yang dikirim:", header_keluar)
      ada_kuota = layanan_jadwal_dokter(header_keluar, kode_poli)
    time.sleep(LAMA_KUNCI_SLOT_DETIK)
    return ada_kuota


if __name__ == "__main__":
  HASIL = layanan_janji_temu(KODE_POLI_CONTOH)
  print("Kuota tersedia:", HASIL)
