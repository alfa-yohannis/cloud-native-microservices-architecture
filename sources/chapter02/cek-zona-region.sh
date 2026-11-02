# Membaca zona dan katalog layanan region Jakarta. Pakai: bash cek-zona-region.sh
#
# Perintah di bawah hanya membaca katalog publik penyedia, tidak membuat
# sumber daya berbayar, dan tidak membebani sistem siapa pun. Akun beserta
# AWS CLI dan Google Cloud CLI (gcloud) yang sudah login tetap diperlukan.
#
# Region Jakarta pada AWS termasuk region opt-in: perintah
# describe-availability-zones baru berhasil setelah region itu diaktifkan di
# pengaturan akun. Parameter katalog layanan bersifat global, sehingga dibaca
# lewat region pembanding yang selalu aktif. Katalog disimpan sebagai
# layanan-aws-<region>.txt, lalu dibandingkan dengan bandingkan_katalog_region.py.

set -euo pipefail

REGION_AWS_JAKARTA="ap-southeast-3"
REGION_AWS_PEMBANDING="us-east-1"
REGION_GOOGLE_JAKARTA="asia-southeast2"
JALUR_KATALOG="/aws/service/global-infrastructure/regions"

# Status opt-in region Jakarta pada akun AWS.
aws ec2 describe-regions --all-regions --region "$REGION_AWS_PEMBANDING" \
  --region-names "$REGION_AWS_JAKARTA" \
  --query 'Regions[].[RegionName,OptInStatus]' --output text

# Nama availability zone di region Jakarta (butuh region yang sudah aktif).
aws ec2 describe-availability-zones --region "$REGION_AWS_JAKARTA" \
  --query 'AvailabilityZones[].ZoneName' --output text

# Katalog layanan AWS, satu nama per baris.
for REGION in "$REGION_AWS_JAKARTA" "$REGION_AWS_PEMBANDING"; do
  aws ssm get-parameters-by-path --region "$REGION_AWS_PEMBANDING" \
    --path "$JALUR_KATALOG/$REGION/services" \
    --query 'Parameters[].Value' --output text \
    | tr '\t' '\n' | sort > "layanan-aws-$REGION.txt"
done

# Nama zona Google Cloud di region Jakarta.
gcloud compute zones list --filter="region:$REGION_GOOGLE_JAKARTA" \
  --format="value(name)"
