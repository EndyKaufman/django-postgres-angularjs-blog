# -*- coding: utf-8 -*-

from project import helpers


def getConfig(request):
    protocol = 'https' if request.is_secure() else 'http'

    config = {}

    config['host'] = '%s://%s' % (protocol, request.get_host())
    config['host_name'] = '%s://%s' % (protocol, request.get_host().decode('idna'))

    user = helpers.get_user(request)

    if not user or user is None:
        config['user'] = {}
    else:
        config['user'] = user.get_ser_data().copy()

    return config
