# Membangun image layanan jadwal dokter. Jalankan di folder ini:
#   docker build -t jadwal-dokter:1.0.0 .
# Image dasar versi slim: ukuran kecil, permukaan serangan lebih sempit.
FROM python:3.12-slim

# Aplikasi berjalan sebagai pengguna biasa, bukan root. Bila aplikasi
# dibobol, penyerang tidak langsung berkuasa penuh atas container.
RUN useradd --create-home --uid 10001 layanan
WORKDIR /app
COPY app.py .
USER layanan

# Nilai bawaan. Nilai sebenarnya diisi saat container dijalankan.
ENV PORT=8080
ENV NAMA_FASILITAS="RS Medikara Jakarta"
EXPOSE 8080

# Satu proses per container, keluarannya langsung ke stdout.
CMD ["python", "app.py"]
