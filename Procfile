release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: env LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUTF8=1 PYTHONIOENCODING=UTF-8 gunicorn controle.wsgi:application --chdir controle --charset=utf-8 --workers ${WEB_CONCURRENCY:-2} --threads ${GUNICORN_THREADS:-2} --timeout 120
