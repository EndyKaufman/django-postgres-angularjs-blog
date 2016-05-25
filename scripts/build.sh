#!/bin/bash

source venv/bin/activate
cd front
gulp build --env development
cd ../
#rm -f db.sqlite3
#python manage.py migrate
python manage.py collectstatic --noinput