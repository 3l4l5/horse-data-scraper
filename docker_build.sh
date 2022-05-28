docker build -t horse-html-scraper .
docker run \
    --name horse-data-scraper \
    --mount type=bind,source=$MOUNT_POINT,target=$MOUNT_POINT \
    horse-html-scraper