# Kebijakan Rego guardrail G1 Bab 14. Pakai: opa eval (perintah di README.md).
package medikara.guardrail.region

# Kode region yang berlokasi di Indonesia (Bab 2). Bila penyedia
# membuka region baru, hanya daftar ini yang diubah lewat review.
region_indonesia := {
  "ap-southeast-3",
  "asia-southeast2",
  "indonesiacentral",
  "ap-batam-1"
}

# Kelas data yang wajib tinggal di Indonesia (Permenkes 24/2022 dan
# UU PDP). Kelas lain diatur guardrail terpisah.
kelas_wajib_lokal := {"rekam-medis", "data-pribadi-spesifik"}

# Pesan dikumpulkan sebagai himpunan agar pipeline menampilkan semua
# pelanggaran sekaligus, bukan berhenti di pelanggaran pertama.
tolak contains pesan if {
  some sumber in input.sumber_daya
  sumber.tag["kelas-data"] in kelas_wajib_lokal
  not sumber.region in region_indonesia
  pesan := sprintf("%s: kelas data %s tidak boleh di region %s",
    [sumber.nama, sumber.tag["kelas-data"], sumber.region])
}

# Tanpa tag kelas data, aturan di atas tidak dapat memutuskan,
# sehingga sumber daya ditolak dan pemiliknya diminta melengkapi.
tolak contains pesan if {
  some sumber in input.sumber_daya
  not sumber.tag["kelas-data"]
  pesan := sprintf("%s: tag kelas-data wajib diisi", [sumber.nama])
}
