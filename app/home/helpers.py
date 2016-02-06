# -*- coding: utf-8 -*-

from app.account.models import User
import django.middleware.csrf


def get(request):
    config = {}

    config['host'] = request.get_host()
    config['hostName'] = request.get_host().decode('idna')
    config['csrf_token'] = django.middleware.csrf.get_token(request)

    try:
        user = User.objects.get(pk=request.user.id)
        config['user'] = user.getUserData().copy()
    except User.DoesNotExist:
        config['user'] = {}


    return config
