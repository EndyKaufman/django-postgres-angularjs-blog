# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q
from django.contrib import auth
from project import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext, get_language
from models import User, Code


def get_fields():
    return [f.name for f in User._meta.get_fields()]


def get_item_by_email(request, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = False
    return user


def get_code(request, text):
    try:
        code = Code.objects.get(text=text)
    except Code.DoesNotExist:
        code = False
    return code


def create(request):
    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    data['email'] = data['email'].lower()

    user = User.objects.create_user(email=data['email'], password=data['password'],
                                    username=data['email'])
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.is_staff = True
    user.is_superuser = False
    user.is_active = True
    user.save()
    user = auth.authenticate(username=user.username, password=data['password'])

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.get_user_data()]}, 200, user
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404, user


def update(request):
    """Update record"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    data['email'] = data['email'].lower()

    user = helpers.get_user(request)
    helpers.json_to_objects(user, data)
    if data['password'] is not None:
        user.set_password(data['password'])
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()

    return {'code': 'ok', 'data': [user.get_user_data()]}, 200, user


def delete(request):
    """Update record"""

    user = helpers.get_user(request)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.delete()

    auth.logout(request)

    return {'code': 'ok'}, 200


def login(request):
    """Login action"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    data['email'] = data['email'].lower()

    user = get_item_by_email(request, data['email'])

    user = auth.authenticate(username=user.username, password=data['password'])

    if user is None:
        return {'code': 'account/nodata'}, 404, False

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.get_user_data()]}, 200, user
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404, False


def logout(request):
    """Logout action"""

    auth.logout(request)
    return {'code': 'ok'}, 200


def recovery(request):
    """Recovery action"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    data['email'] = data['email'].lower()

    user = get_item_by_email(request, data['email'])

    code = Code.objects.create(text=helpers.make_code(), created_user=user, type=1)

    from ..home.helpers import get_config
    from ..manager.properties import resource as properties_resource

    config = get_config(request)
    config['code'] = code.text
    config['user_first_name'] = user.first_name
    config['properties'] = properties_resource.get_list_of_names(['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME',
                                                                  'SITE_LOGO'])
    helpers.send_mail(subject=ugettext('Reset password'),
                      html_content=render_to_string(
                          'account/templates/%s/%s/reset.email.htm' % (settings.THEME, get_language()), config),
                      text_content=render_to_string(
                          'account/templates/%s/%s/reset.email.txt' % (settings.THEME, get_language()), config),
                      to_email=[data['email']],
                      config=config)

    return {'code': 'ok', 'data': [data['email']]}, 200, user


def reset(request):
    """Reset password action"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    data['code'] = data['code'].lower()

    code = get_code(request, data['code'])

    if code:
        try:
            user = User.objects.get(pk=code.created_user.id)
        except User.DoesNotExist:
            user = False

    if user.is_active and code:

        if data['password'] is not None:
            user.set_password(data['password'])
        helpers.json_to_objects(user, data)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()

        auth.login(request, user)
        code.delete()

        return {'code': 'ok', 'data': [user.get_user_data()]}, 200, user
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404, False
