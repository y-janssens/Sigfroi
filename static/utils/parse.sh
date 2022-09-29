#!/bin/bash
uuid=$1

python manage.py dumpdata --exclude auth.permission --exclude contenttypes > ./static/backups/$uuid.json