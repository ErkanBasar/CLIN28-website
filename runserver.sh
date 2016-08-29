#!/bin/bash

ROOTDIR=/scratch2/www/ATILA-2016/

. /scratch2/www/ATILA-2016/env/bin/activate

#python3 manage.py runserver 3039
uwsgi --virtualenv $VIRTUAL_ENV --socket 127.0.0.1:3039 --chdir $ROOTDIR --wsgi-file $ROOTDIR/Atila16/wsgi.py --logto $ROOTDIR/atila16.uwsgi.log --log-date --log-5xx --master --processes 4 --threads 2 --need-app --pidfile ./atila16.pid --py-autoreload 1
