# -*- coding: utf-8 -*-

import django.middleware.csrf


def getConfig(request):
    config = {}
    config['host'] = request.get_host()
    config['hostName'] = request.get_host().decode('idna')
    config['user'] = {}

    return config
