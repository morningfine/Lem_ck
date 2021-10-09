#!/bin/sh
set -e
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('lemon1', 'lemon100@qq.com', '123456')" | python manage.py shell &> /dev/null
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('keyou1', 'keyou100@qq.com', '123456')" | python manage.py shell &> /dev/null
/usr/local/bin/gunicorn -c /usr/src/app/configs/gunicorn_config.py dev07.wsgi