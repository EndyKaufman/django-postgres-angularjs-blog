# -*- coding: utf-8 -*-

import json
from app.myauth.config import getUserData
import django.middleware.csrf
from django.contrib.staticfiles.templatetags.staticfiles import static


def get(request):
    config = {}

    try:
        with open('app/home/fixtures/config.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    config = json.loads(content)

    config['host'] = request.get_host()
    config['hostName'] = request.get_host().decode('idna')
    config['csrf_token'] = django.middleware.csrf.get_token(request)
    config['static_url'] = static('')

    userDataConfig = getUserData(request).copy()
    config.update(userDataConfig)

    return config
