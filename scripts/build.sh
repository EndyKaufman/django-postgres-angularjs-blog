#!/bin/bash

source venv/bin/activate
cd front
ls
gulp build --env development
cd ../
ls
rm -f db.sqlite3
python -c "import sys; print((sys.path))"                                           
python -c "import django; print(django.get_version())"                                                        
python manage.py migrate
python manage.py collectstatic --noinput