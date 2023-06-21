set -eux

export TZ="Asia/Tokyo"

curl -o /dev/null -s -X POST https://content.dropboxapi.com/2/files/upload --header "Authorization: Bearer ${DROPBOX_TOKEN}" \
    --header "Dropbox-API-Arg: {\"path\": \"/Splatoon3/$1/$2\",\"mode\": \"overwrite\",\"mute\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @$2
