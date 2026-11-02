# Pembanding empat strategi DR Bab 12. Jalankan python bandingkan-strategi-dr.py
"""Membandingkan biaya empat strategi DR untuk setiap layanan.

Total biaya tahunan = biaya DR + perkiraan kerugian tahunan. Perkiraan
kerugian tahunan = frekuensi kejadian besar per tahun x RTO strategi x
kerugian per jam. Strategi yang dipilih adalah strategi termurah yang
memenuhi RTO dan RPO target. Strategi termurah tanpa syarat juga dicetak,
karena selisih keduanya adalah harga yang dibayar demi target bisnis.

Cara memakai dengan data tim: siapkan CSV berkolom layanan,
kerugian_per_jam_juta, biaya_produksi_juta, rto_target_jam, rpo_target_menit,
lalu jalankan: python bandingkan-strategi-dr.py data-tim.csv
Semua angka bawaan adalah rekaan untuk kasus fiktif Medikara Health.
"""

import csv
import sys

FREKUENSI_KEJADIAN_PER_TAHUN = 0.5

# Profil kasar setiap strategi: RTO dalam jam, RPO dalam menit, dan biaya DR
# sebagai rasio terhadap biaya infrastruktur produksi per tahun.
PROFIL_STRATEGI = [
    ("backup and restore", 12.0, 60.0, 0.08),
    ("pilot light", 2.0, 5.0, 0.20),
    ("warm standby", 0.5, 1.0, 0.45),
    ("multi-site active-active", 0.1, 0.1, 1.25),
]

# Data bawaan dalam juta rupiah, sama dengan angka di naskah Bab 12.
LAYANAN_BAWAAN = [
    {"layanan": "Rekam medis elektronik", "kerugian_per_jam_juta": 150,
     "biaya_produksi_juta": 1200, "rto_target_jam": 1,
     "rpo_target_menit": 5},
    {"layanan": "Medikara+", "kerugian_per_jam_juta": 40,
     "biaya_produksi_juta": 600, "rto_target_jam": 4,
     "rpo_target_menit": 15},
    {"layanan": "ERP keuangan", "kerugian_per_jam_juta": 15,
     "biaya_produksi_juta": 800, "rto_target_jam": 24,
     "rpo_target_menit": 60},
]


def baca_csv(jalur):
    """Membaca data layanan tim dan mengubah kolom angka menjadi float."""
    kolom_angka = ["kerugian_per_jam_juta", "biaya_produksi_juta",
                   "rto_target_jam", "rpo_target_menit"]
    with open(jalur, encoding="utf-8") as berkas:
        baris_data = [baris for baris in csv.DictReader(berkas)]
    for baris in baris_data:
        for kolom in kolom_angka:
            baris[kolom] = float(baris[kolom])
    return baris_data


def hitung_strategi(layanan):
    """Menghitung biaya, kerugian, dan kecocokan target untuk tiap strategi.

    Hasilnya daftar baris agar mudah dicetak dan dibandingkan.
    """
    hasil = []
    for nama, rto_jam, rpo_menit, rasio_biaya in PROFIL_STRATEGI:
        biaya_dr = rasio_biaya * layanan["biaya_produksi_juta"]
        kerugian = (FREKUENSI_KEJADIAN_PER_TAHUN * rto_jam
                    * layanan["kerugian_per_jam_juta"])
        memenuhi = (rto_jam <= layanan["rto_target_jam"]
                    and rpo_menit <= layanan["rpo_target_menit"])
        hasil.append({"strategi": nama, "rto_jam": rto_jam,
                      "biaya_dr": biaya_dr, "kerugian": kerugian,
                      "total": biaya_dr + kerugian, "memenuhi": memenuhi})
    return hasil


def ambil_total(baris):
    """Kunci pengurutan: strategi dibandingkan menurut total biaya tahunan."""
    return baris["total"]


def cetak_layanan(layanan):
    """Mencetak tabel satu layanan beserta strategi yang disarankan."""
    hasil = hitung_strategi(layanan)
    print(f"\n{layanan['layanan']} (RTO {layanan['rto_target_jam']:g} jam, "
          f"RPO {layanan['rpo_target_menit']:g} menit)")
    print(f"  {'strategi':26s}{'RTO':>6s}{'biaya DR':>10s}"
          f"{'kerugian':>10s}{'total':>10s}  target")
    for baris in hasil:
        tanda = "ya" if baris["memenuhi"] else "tidak"
        print(f"  {baris['strategi']:26s}{baris['rto_jam']:6.1f}"
              f"{baris['biaya_dr']:10.1f}{baris['kerugian']:10.1f}"
              f"{baris['total']:10.1f}  {tanda}")
    termurah = min(hasil, key=ambil_total)
    memenuhi = [baris for baris in hasil if baris["memenuhi"]]
    print(f"  termurah tanpa syarat : {termurah['strategi']}")
    if memenuhi:
        pilihan = min(memenuhi, key=ambil_total)
        print(f"  termurah yang memenuhi: {pilihan['strategi']}")
    else:
        print("  tidak ada strategi yang memenuhi target; tinjau ulang target")


if __name__ == "__main__":
    daftar = baca_csv(sys.argv[1]) if len(sys.argv) > 1 else LAYANAN_BAWAAN
    print("Angka dalam juta rupiah per tahun; RTO dalam jam.")
    for satu_layanan in daftar:
        cetak_layanan(satu_layanan)
