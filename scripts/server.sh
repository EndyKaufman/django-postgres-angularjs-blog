#!/bin/bash

source venv/bin/activate
ls
python -c "import sys; print((sys.path))"
python -c "import django; print(django.get_version())"
gunicorn project.wsgi -b 0.0.0.0:5000