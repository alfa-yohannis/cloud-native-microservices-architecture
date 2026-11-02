# Sumber Bab 14

Berkas pendukung Bab 14, Peta Jalan Modernisasi dan Tata Kelola Cloud. Seluruh angka di dalamnya
rekaan untuk kasus fiktif Medikara Health. Berkas dipakai pada Aktivitas "Peta Jalan Modernisasi dan
Guardrail Tata Kelola", pada kotak pendalaman teknis, dan pada Latihan.

| Berkas | Kegunaan |
| :-- | :-- |
| `templat-peta-jalan-modernisasi.xlsx` | Templat peta jalan tiga gelombang. Lembar "Contoh Medikara" berisi rencana rekaan Bab 14, lembar "Isian Tim" dipakai untuk organisasi tim, dan lembar "Kartu Metrik" memuat nilai awal serta sasaran per gerbang keputusan. |
| `katalog-guardrail.md` | Tujuh contoh *guardrail* Medikara dengan jenis kendali, risiko, bukti, pemilik, dan jalur pengecualian, ditambah lembar isian tim dan daftar periksa. Dipakai pada Aktivitas dan Latihan 2. |
| `templat-presentasi-c4.md` | Susunan presentasi tonggak C4 selama 15 menit, isian slide, dan pertanyaan latihan tanya jawab. |
| `contoh-opa/guardrail-region.rego` | Kebijakan Rego (sintaks OPA 1.x) untuk pendalaman teknis: menolak sumber daya berkelas rekam medis di luar *region* Indonesia dan sumber daya tanpa tag kelas data. |
| `contoh-opa/rencana-sumber-daya.json` | Masukan rekaan untuk kebijakan di atas, berisi empat sumber daya. Format disederhanakan, bukan format asli rencana Terraform. JSON tidak mengenal komentar, sehingga keterangan berkas ditaruh pada kunci `_keterangan` di baris pertama. |

Cara menjalankan kebijakan contoh, bila Open Policy Agent sudah terpasang:

```bash
cd sources/chapter14/contoh-opa
opa eval -d guardrail-region.rego -i rencana-sumber-daya.json \
  "data.medikara.guardrail.region.tolak"
```

Hasil yang diharapkan: dua pesan penolakan, yaitu `cadangan-rekam-medis` di *region*
`ap-southeast-1` dan `log-uji-beban` yang tidak punya tag kelas data. `situs-informasi-publik`
lolos karena kelas datanya publik.

Kebijakan ini belum dijalankan pada mesin penulis naskah karena OPA tidak terpasang di sana. Mahasiswa
mencoba kebijakan pada akun atau berkas milik tim sendiri. Data organisasi nyata dipakai seizin
organisasi dan dianonimkan. Data pribadi pasien atau karyawan tidak dipakai.
