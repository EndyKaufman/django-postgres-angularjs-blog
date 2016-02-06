# -*- coding: utf-8 -*-

import json
from app.myauth.helpers import getUserData
import django.middleware.csrf
from django.contrib.staticfiles.templatetags.staticfiles import static


def get(request):
    config = {}

    config['host'] = request.get_host()
    config['hostName'] = request.get_host().decode('idna')
    config['csrf_token'] = django.middleware.csrf.get_token(request)
    config['static_url'] = static('')
    config['user'] = getUserData(request.user).copy()

    return config
