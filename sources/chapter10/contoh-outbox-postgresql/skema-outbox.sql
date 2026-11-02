-- Skema contoh outbox Bab 10. Muat dengan: psql -d medikara -f skema-outbox.sql
-- Untuk PostgreSQL 13 atau lebih baru milik sendiri; seluruh datanya rekaan.

-- Tabel bisnis milik Layanan Jadwal. Layanan lain tidak boleh menulis ke tabel ini.
CREATE TABLE IF NOT EXISTS jadwal_dokter (
  id_slot     text PRIMARY KEY,
  id_dokter   text NOT NULL,
  mulai       timestamptz NOT NULL,
  status      text NOT NULL DEFAULT 'TERSEDIA',
  id_rujukan  text
);

-- Tabel outbox. Setiap baris adalah satu event yang menunggu diterbitkan.
-- id_event dipakai consumer untuk menolak event yang datang dua kali.
CREATE TABLE IF NOT EXISTS outbox (
  id            bigserial PRIMARY KEY,
  id_event      uuid NOT NULL DEFAULT gen_random_uuid(),
  jenis_event   text NOT NULL,
  id_agregat    text NOT NULL,
  isi           jsonb NOT NULL,
  waktu_dibuat  timestamptz NOT NULL DEFAULT now(),
  waktu_terbit  timestamptz
);

-- Indeks parsial: penerbit hanya mencari baris yang belum terbit, sehingga indeks
-- tetap kecil walaupun tabel outbox sudah berisi banyak baris lama.
CREATE INDEX IF NOT EXISTS outbox_belum_terbit
  ON outbox (id) WHERE waktu_terbit IS NULL;

-- Satu slot rekaan untuk dicoba.
INSERT INTO jadwal_dokter (id_slot, id_dokter, mulai)
VALUES ('SLOT-BKS-0915', 'DR-BKS-017', '2026-11-09 09:15+07')
ON CONFLICT DO NOTHING;

-- Transaksi lokal: mengunci slot dan mencatat event JadwalDikunci.
-- Baris outbox hanya tercipta bila slot benar-benar berhasil dikunci,
-- dan keduanya tersimpan atau batal bersama.
BEGIN;
WITH slot_terkunci AS (
  UPDATE jadwal_dokter
  SET status = 'DIKUNCI', id_rujukan = 'RJK-2026-11-00042'
  WHERE id_slot = 'SLOT-BKS-0915' AND status = 'TERSEDIA'
  RETURNING id_slot, id_dokter, id_rujukan
)
INSERT INTO outbox (jenis_event, id_agregat, isi)
SELECT 'JadwalDikunci', id_slot,
  jsonb_build_object('id_rujukan', id_rujukan, 'id_dokter', id_dokter)
FROM slot_terkunci;
COMMIT;
