#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

cd Chatter

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py shell -c "from django.db import connection; print('DB_HOST:', connection.settings_dict['HOST']); print('DB_NAME:', connection.settings_dict['NAME']); print('DB_USER:', connection.settings_dict['USER'])"