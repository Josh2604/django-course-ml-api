#!/bin/sh
#  /usr/local/bin/gunicorn --bind=0.0.0.0 --timeout 600 users_api.wsgi
gunicorn --bind=0.0.0.0 --timeout 600 users_api.wsgi