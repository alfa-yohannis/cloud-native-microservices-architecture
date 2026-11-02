# Simulasi circuit breaker Bab 12. Jalankan python simulasi-circuit-breaker.py
"""Membandingkan pemanggil tanpa dan dengan circuit breaker.

Layanan pendaftaran Medikara memeriksa kepesertaan pasien ke layanan pihak
ketiga satu kali per detik. Layanan pihak ketiga sengaja dibuat gangguan pada
detik 20 sampai 79. Waktu dihitung dalam detik simulasi, bukan detik nyata,
sehingga skrip selesai seketika dan hasilnya selalu sama setiap dijalankan.
Hanya pustaka standar Python yang dipakai, jadi tidak ada yang perlu dipasang.
"""

LAMA_SIMULASI_DETIK = 120
GANGGUAN_MULAI_DETIK = 20
GANGGUAN_SELESAI_DETIK = 80
BATAS_WAKTU_DETIK = 3.0
WAKTU_RESPONS_NORMAL_DETIK = 0.8
AMBANG_GAGAL_BERUNTUN = 5
LAMA_TERBUKA_DETIK = 30

TERTUTUP = "tertutup"
TERBUKA = "terbuka"
SETENGAH_TERBUKA = "setengah terbuka"


def tujuan_sehat(detik):
    """Menentukan apakah layanan pihak ketiga sehat pada detik tertentu.

    Gangguan dibuat terjadwal, bukan acak, agar hasil dua perilaku dapat
    dibandingkan secara adil pada kejadian yang sama.
    """
    return not GANGGUAN_MULAI_DETIK <= detik < GANGGUAN_SELESAI_DETIK


class PemutusSirkuit:
    """Circuit breaker sederhana dengan tiga keadaan.

    Kegagalan beruntun dihitung. Bila ambang tercapai, panggilan langsung
    ditolak selama lama_terbuka detik. Akibatnya pemanggil tidak ikut
    tertahan dan layanan tujuan diberi waktu untuk pulih.
    """

    def __init__(self, ambang_gagal, lama_terbuka):
        self.ambang_gagal = ambang_gagal
        self.lama_terbuka = lama_terbuka
        self.keadaan = TERTUTUP
        self.gagal_beruntun = 0
        self.dibuka_pada = 0
        self.riwayat = []

    def pindah(self, detik, keadaan_baru):
        """Mengganti keadaan dan mencatatnya agar perilaku dapat diamati."""
        if keadaan_baru != self.keadaan:
            self.riwayat.append((detik, self.keadaan, keadaan_baru))
            self.keadaan = keadaan_baru

    def boleh_memanggil(self, detik):
        """Menjawab apakah panggilan boleh diteruskan ke layanan tujuan.

        Setelah lama_terbuka habis, satu panggilan uji diizinkan lewat.
        """
        if self.keadaan != TERBUKA:
            return True
        if detik - self.dibuka_pada >= self.lama_terbuka:
            self.pindah(detik, SETENGAH_TERBUKA)
            return True
        return False

    def catat_berhasil(self, detik):
        """Satu keberhasilan menutup sirkuit dan mengosongkan hitungan."""
        self.gagal_beruntun = 0
        self.pindah(detik, TERTUTUP)

    def catat_gagal(self, detik):
        """Kegagalan menambah hitungan dan dapat membuka sirkuit.

        Pada keadaan setengah terbuka, satu kegagalan langsung membuka
        kembali sirkuit, karena tujuan terbukti belum pulih.
        """
        self.gagal_beruntun += 1
        if (self.keadaan == SETENGAH_TERBUKA
                or self.gagal_beruntun >= self.ambang_gagal):
            self.dibuka_pada = detik
            self.pindah(detik, TERBUKA)


def jalankan(pemutus):
    """Menjalankan simulasi dan mengembalikan ringkasan angka.

    Bila pemutus bernilai None, setiap panggilan diteruskan ke tujuan dan
    menunggu sampai batas waktu bila tujuan gangguan. Bila pemutus ada,
    panggilan yang ditolak dialihkan ke jalur cadangan: kepesertaan dicatat
    untuk diperiksa ulang, dan pasien tetap didaftarkan.
    """
    ringkasan = {"berhasil": 0, "gagal_menunggu": 0, "dialihkan": 0,
                 "total_tunggu_detik": 0.0}
    for detik in range(LAMA_SIMULASI_DETIK):
        if pemutus and not pemutus.boleh_memanggil(detik):
            ringkasan["dialihkan"] += 1
        elif tujuan_sehat(detik):
            ringkasan["berhasil"] += 1
            ringkasan["total_tunggu_detik"] += WAKTU_RESPONS_NORMAL_DETIK
            if pemutus:
                pemutus.catat_berhasil(detik)
        else:
            ringkasan["gagal_menunggu"] += 1
            ringkasan["total_tunggu_detik"] += BATAS_WAKTU_DETIK
            if pemutus:
                pemutus.catat_gagal(detik)
    return ringkasan


def cetak(judul, ringkasan, pemutus):
    """Mencetak ringkasan agar dua perilaku mudah dibandingkan."""
    print(judul)
    for detik, dari, ke in (pemutus.riwayat if pemutus else []):
        print(f"  detik {detik:3d}: {dari} -> {ke}")
    print(f"  berhasil                : {ringkasan['berhasil']}")
    print(f"  gagal setelah menunggu  : {ringkasan['gagal_menunggu']}")
    print(f"  dialihkan ke cadangan   : {ringkasan['dialihkan']}")
    print(f"  total waktu tunggu      : "
          f"{ringkasan['total_tunggu_detik']:.1f} detik")


if __name__ == "__main__":
    cetak("Tanpa circuit breaker", jalankan(None), None)
    pemutus_uji = PemutusSirkuit(AMBANG_GAGAL_BERUNTUN, LAMA_TERBUKA_DETIK)
    cetak("Dengan circuit breaker", jalankan(pemutus_uji), pemutus_uji)
