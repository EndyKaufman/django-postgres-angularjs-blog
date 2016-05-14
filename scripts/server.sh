#!/bin/bash

source venv/bin/activate
gunicorn project.wsgi -b 0.0.0.0:5000 --workers 3