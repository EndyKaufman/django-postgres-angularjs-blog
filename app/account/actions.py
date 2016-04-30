# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from django.conf import settings
import resource
import validator


@json_view
def update(request):
    """Update record"""

    data, code, valid = validator.update(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, user = resource.update(request)
            except:
                return {'code': 'account/update/fail'}, 404
        else:
            data, code, user = resource.update(request)

    return data, code


# Login
@json_view
def login(request):
    """Login action"""

    data, code, valid = validator.login(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, user = resource.login(request)
            except:
                return {'code': 'account/login/fail'}, 404
        else:
            data, code, user = resource.login(request)

    return data, code


@json_view
def reg(request):
    """Reg action"""
    data, code, valid = validator.create(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, user = resource.create(request)
            except:
                return {'code': 'account/create/fail'}, 404
        else:
            data, code, user = resource.create(request)

    return data, code


@json_view
def delete(request):
    """Delete record"""

    data, code, valid = validator.delete(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code = resource.delete(request)
            except:
                return {'code': 'account/delete/fail'}, 404
        else:
            data, code = resource.delete(request)

    return data, code


# Logout
@json_view
def logout(request):
    """Logout action"""

    data, code, valid = validator.logout(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code = resource.logout(request)
            except:
                return {'code': 'account/logout/fail'}, 404
        else:
            data, code = resource.logout(request)

    return data, code


@json_view
def recovery(request):
    """Recovery action"""

    data, code, valid = validator.recovery(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, user = resource.recovery(request)
            except:
                return {'code': 'account/recovery/fail'}, 404
        else:
            data, code, user = resource.recovery(request)

    return data, code


# Reset password
@json_view
def reset_password(request):
    """Reset password action"""

    data, code, valid = validator.reset_password(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, user = resource.reset_password(request)
            except:
                return {'code': 'account/reset_password/fail'}, 404
        else:
            data, code, user = resource.reset_password(request)

    return data, code
