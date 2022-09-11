#!/bin/bash
uuid=$1
python manage.py loaddata ./static/backups/$uuid.json