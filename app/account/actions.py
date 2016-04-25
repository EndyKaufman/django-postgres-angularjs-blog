# -*- coding: utf-8 -*-

from django.contrib import auth
from jsonview.decorators import json_view
from project import helpers
from app import home
from django.conf import settings
from django.template.loader import render_to_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import helpers as account_helpers


# update profile
@json_view
def actionUpdate(request):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email', 'password', 'username', 'firstname', 'lastname'])

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404

    try:
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
    except:
        return {'code': 'account/update/fail'}, 404

    return {'code': 'ok', 'data': [user.getUserData()]}


# Login
@json_view
def actionLogin(request):
    """Login action"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email', 'password'])

    if json_data['password'] is None:
        return {'code': 'account/no_password'}, 404

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    user = account_helpers.getUserByEmail(json_data['email'])

    if not user:
        return {'code': 'account/user_not_found', 'values': [json_data['email']]}, 404

    user = auth.authenticate(username=user.username, password=json_data['password'])

    if user is None:
        return {'code': 'account/nodata'}, 404

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404


# create
@json_view
def actionReg(request):
    """Reg action"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email', 'password'])

    if json_data['password'] is None:
        return {'code': 'account/no_password'}, 404

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    user = account_helpers.getUserByEmail(json_data['email'])

    if user:
        return {'code': 'account/exists', 'values': [json_data['email']]}, 404

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

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404


# delete account
@json_view
def actionDelete(request):
    """Delete record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.delete()

    auth.logout(request)

    return {'code': 'ok'}


# Logout
@json_view
def actionLogout(request):
    """Logout action"""

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    auth.logout(request)
    return {'code': 'ok'}


# Recovery
@json_view
def actionRecovery(request):
    """Recovery action"""

    if request.user.is_authenticated():
        return {'code': 'no_access'}, 404

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email'])

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    from app.account.models import Code

    user = account_helpers.getUserByEmail(json_data['email'])

    if not user:
        return {'code': 'account/user_not_found', 'values': [json_data['email']]}, 404

    code = Code.objects.create(text=helpers.makeCode(), created_user=user, type=1)

    config = home.helpers.getConfig(request)
    config['code'] = code.text
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['user_first_name'] = user.first_name

    helpers.sendmail(subject='Reset password',
                     html_content=render_to_string('account/templates/resetpassword.email.htm', config),
                     text_content=render_to_string('account/templates/resetpassword.email.txt', config),
                     to_email=[json_data['email']])

    return {'code': 'ok', 'data': [json_data['email']]}


# Reset password
@json_view
def actionResetpassword(request):
    """Reset password action"""

    if request.user.is_authenticated():
        return {'code': 'no_access'}, 404

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['code', 'password'])

    if json_data['code'] is None:
        return {'code': 'account/no_code'}, 404

    json_data['code'] = json_data['code'].lower()

    if json_data['password'] is None:
        return {'code': 'account/no_password'}, 404

    user, code = account_helpers.getUserByCode(json_data['code'])

    if not code:
        return {'code': 'account/code_not_found', 'values': [json_data['code']]}, 404

    if user.is_active and code:
        try:
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
        except:
            return {'code': 'account/update/fail'}, 404
        auth.login(request, user)
        code.delete()

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/not_active'}, 404
