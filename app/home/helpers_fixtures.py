# -*- coding: utf-8 -*-

import django.middleware.csrf
from django.contrib.staticfiles.templatetags.staticfiles import static


def getConfig(request):
    config = {}
    config['host'] = request.get_host()
    config['hostName'] = request.get_host().decode('idna')
    config['csrf_token'] = django.middleware.csrf.get_token(request)
    config['static_url'] = static('')
    config['user'] = {}

    return config
