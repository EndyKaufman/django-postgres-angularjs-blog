# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q
from django.contrib import auth
from project import settings
from django.template.loader import render_to_string

def get_fields():
    return ['email', 'password', 'username', 'firstname', 'lastname']

def get_item_by_email(request, email):
    from app.account.models import User
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = False
    return user


def get_code(request, text):
    from app.account.models import Code
    try:
        code = Code.objects.get(text=text)
    except Code.DoesNotExist:
        code = False
    return code


def create(request):
    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data,get_fields())

    json_data['email'] = json_data['email'].lower()

    from app.account.models import User

    user = User.objects.create_user(email=json_data['email'], password=json_data['password'],
                                    username=json_data['email'])
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.is_staff = True
    user.is_superuser = False
    user.is_active = True
    user.save()
    user = auth.authenticate(username=user.username, password=json_data['password'])

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.getUserData()]}, 200, user
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404, user


def update(request):
    """Update record"""

    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data,get_fields())

    json_data['email'] = json_data['email'].lower()

    user = helpers.getUser(request)

    if json_data['email'] is not None:
        user.email = json_data['email']

    if json_data['password'] is not None:
        user.set_password(json_data['password'])

    if json_data['username'] is not None:
        user.username = json_data['username']

    if json_data['firstname'] is not None:
        user.first_name = json_data['firstname']

    if json_data['lastname'] is not None:
        user.last_name = json_data['lastname']

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()

    return {'code': 'ok', 'data': [user.getUserData()]}, 200, user


def delete(request):
    """Update record"""

    user = helpers.getUser(request)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.delete()

    auth.logout(request)

    return {'code': 'ok'}, 200


def login(request):
    """Login action"""

    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data,get_fields())

    json_data['email'] = json_data['email'].lower()

    user = get_item_by_email(request, json_data['email'])

    user = auth.authenticate(username=user.username, password=json_data['password'])

    if user is None:
        return {'code': 'account/nodata'}, 404, False

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.getUserData()]}, 200, user
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404, False


def logout(request):
    """Logout action"""

    auth.logout(request)
    return {'code': 'ok'}, 200


def recovery(request):
    """Recovery action"""

    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, get_fields())

    json_data['email'] = json_data['email'].lower()

    from app.account.models import Code

    user = get_item_by_email(request, json_data['email'])

    code = Code.objects.create(text=helpers.makeCode(), created_user=user, type=1)

    from app import home

    config = home.helpers.getConfig(request)
    config['code'] = code.text
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['user_first_name'] = user.first_name

    helpers.sendmail(subject='Reset password',
                     html_content=render_to_string('account/templates/resetpassword.email.htm', config),
                     text_content=render_to_string('account/templates/resetpassword.email.txt', config),
                     to_email=[json_data['email']])

    return {'code': 'ok', 'data': [json_data['email']]}, 200, user


def reset_password(request):
    """Reset password action"""

    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data,get_fields())

    json_data['code'] = json_data['code'].lower()

    code = get_code(request, json_data['code'])

    from app.account.models import User

    if code:
        try:
            user = User.objects.get(pk=code.created_user.id)
        except User.DoesNotExist:
            user = False

    if user.is_active and code:
        if json_data['email'] is not None:
            user.email = json_data['email']

        if json_data['password'] is not None:
            user.set_password(json_data['password'])

        if json_data['username'] is not None:
            user.username = json_data['username']

        if json_data['firstname'] is not None:
            user.first_name = json_data['firstname']

        if json_data['lastname'] is not None:
            user.last_name = json_data['lastname']

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()

        auth.login(request, user)
        code.delete()

        return {'code': 'ok', 'data': [user.getUserData()]}, 200, user
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404, False
