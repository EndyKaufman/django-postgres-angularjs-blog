#!/bin/bash

source venv/bin/activate
# rm -f db.sqlite3
# python manage.py migrate
cd front
gulp build --env development
cd ../
python manage.py collectstatic --noinput