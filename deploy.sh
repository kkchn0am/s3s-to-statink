set -eux

export TZ="Asia/Tokyo"

TIMESTAMP=$(date "+%Y%m%d-%H%M%S")

curl -X POST -f -H "Authorization: Bearer ${DROPBOX_TOKEN}" \
    -D - -H "Dropbox-API-Arg: {\"path\": \"/${TIMESTAMP}.*\",\"mode\": \"overwrite\",\"mute\": false}" \
    -H "Content-Type: application/octet-stream" \
    --data-binary @log.txt \
    https://content.dropboxapi.com/2/files/upload
