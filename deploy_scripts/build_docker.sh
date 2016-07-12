#!/usr/bin/env bash

cd /web
docker-compose -f test.yml build
docker-compose -f test.yml up -d
docker run --net="web_default" web_pycharm python manage.py makemigrations
docker run --net="web_default" web_pycharm python manage.py migrate
