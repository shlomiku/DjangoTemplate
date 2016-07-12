#!/usr/bin/env bash

cd /web
docker stop `docker ps -q`
docker-compose -f test.yml down
docker-compose -f test.yml down web_pycharm
# if that didn't work
docker rm -f `docker ps -qa`

