# -*- coding: utf-8 -*-

from project import helpers

def getConfig(request):
    protocol = 'https' if request.is_secure() else 'http'

    config = {}

    config['host'] = '%s://%s' % (protocol, request.get_host())
    config['hostName'] = '%s://%s' % (protocol, request.get_host().decode('idna'))

    user = helpers.getUser(request)

    if not user or user is None:
        config['user'] = {}
    else:
        config['user'] = user.getUserData().copy()

    return config
