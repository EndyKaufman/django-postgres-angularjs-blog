# -*- coding: utf-8 -*-

from app.account.models import User
import django.middleware.csrf


def getConfig(request):
    protocol = 'https' if request.is_secure() else 'http'

    config = {}

    config['host'] = '%s://%s' % (protocol, request.get_host())
    config['hostName'] = '%s://%s' % (protocol, request.get_host().decode('idna'))

    try:
        user = User.objects.get(pk=request.user.id)
        config['user'] = user.getUserData().copy()
    except User.DoesNotExist:
        config['user'] = {}

    return config
