docker stop pipe_to_bash
docker rm pipe_to_bash
docker run \
       --name pipe_to_bash \
       -e DB_USER="" \
       -e DB_PASS="" \
       -e WP_DB_NAME="" \
       -e WP_DB_HOST="" \
       -e VIRTUAL_HOST=pipe-to-bash.today \
       -e PTBT_DEPLOYMENT="dev" \
       -e PTBT_PORT=80 \
       -d \
       --restart=always \
       pipe-to-bash:latest
