#!/usr/bin/env bash

cd /web
docker run --net="web_default" -p 8000:8000 -d web_pycharm python manage.py runserver 0.0.0.0:8000
