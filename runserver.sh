#!/bin/bash

ROOTDIR=/scratch2/www/CLIN28/

. /scratch2/www/CLIN28/env/bin/activate

#python3 manage.py runserver 2546
uwsgi --virtualenv $VIRTUAL_ENV --socket 127.0.0.1:2546 --chdir $ROOTDIR --wsgi-file $ROOTDIR/CLIN28/wsgi.py --logto $ROOTDIR/clin28.uwsgi.log --log-date --log-5xx --master --processes 4 --threads 2 --need-app --pidfile ./clin28.pid --py-autoreload 1
