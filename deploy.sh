set -eux

export TZ="Asia/Tokyo"

TIMESTAMP=$(date "+%Y%m%d-%H%M%S")

curl -vso /dev/null -X POST https://content.dropboxapi.com/2/files/upload --header "Authorization: Bearer ${DROPBOX_TOKEN}" \
    --header "Dropbox-API-Arg: {\"path\": \"/$1\",\"mode\": \"overwrite\",\"mute\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @$1
