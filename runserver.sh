#!/bin/bash

ROOTDIR=/scratch2/www/PICA/

. /scratch2/www/PICA/env/bin/activate

#python3 manage.py runserver 2546
uwsgi --virtualenv $VIRTUAL_ENV --socket 127.0.0.1:2598 --chdir $ROOTDIR --wsgi-file $ROOTDIR/PICA/wsgi.py --logto $ROOTDIR/pica.uwsgi.log --log-date --log-5xx --master --processes 4 --threads 2 --need-app --pidfile ./pica.pid --py-autoreload 1
