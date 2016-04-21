# -*- coding: utf-8 -*-

from django.contrib import auth
import json
from jsonview.decorators import json_view
from project import helpers
from helpers import validateLogin, updateFromJsonObject, validateProfileUpdate, \
    validateRecovery, validateResetpassword
from app import home
from django.conf import settings
from django.template.loader import render_to_string


# update profile
@json_view
def actionUpdate(request):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user:
        return {'code': 'noaccess'}, 404

    validateResult, validateCode = validateProfileUpdate(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    # try:
    validateResult, validateCode = updateFromJsonObject(user, json_data)
    if validateCode != 200:
        return validateResult, validateCode

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    # except:
    #    return {'code': 'account/update/fail'}, 404

    return {'code': 'ok', 'data': [user.getUserData()]}


# Login
@json_view
def actionLogin(request):
    """Login action"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if user:
        return {'code': 'noaccess'}, 404

    from app.account.models import User

    validateResult, validateCode = validateLogin(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except:
        emailField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = ''

    try:
        user = User.objects.get(email=emailField)
    except User.DoesNotExist:
        return {'code': 'account/usernotfound', 'values': [emailField]}, 404

    user = auth.authenticate(username=user.username, password=passwordField)

    if user is None:
        return {'code': 'account/wrongpassword'}, 404

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/notactive'}, 404


# create
@json_view
def actionReg(request):
    """Reg action"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if user:
        return {'code': 'noaccess'}, 404

    from app.account.models import User

    validateResult, validateCode = validateLogin(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except:
        emailField = ''
    try:
        passwordField = json_data['password']
    except:
        passwordField = ''

    try:
        user = User.objects.get(email=emailField)
    except User.DoesNotExist:
        user = False

    if user != False:
        return {'code': 'account/exists', 'values': [emailField]}, 404

    user = User.objects.create_user(email=emailField, password=passwordField, username=emailField)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.is_staff = True
    user.is_superuser = False
    user.is_active = True
    user.save()
    user = auth.authenticate(username=user.username, password=passwordField)

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/notactive'}, 404


# delete account
@json_view
def actionDelete(request):
    """Delete record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user:
        return {'code': 'noaccess'}, 404

    user = helpers.getUser(request)

    if not user:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

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
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

    auth.logout(request)
    return {'code': 'ok'}


# Recovery
@json_view
def actionRecovery(request):
    """Recovery action"""

    if request.user.is_authenticated():
        return {'code': 'noaccess'}, 404

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User, Code

    validateResult, validateCode = validateRecovery(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except:
        emailField = ''

    try:
        user = User.objects.get(email=emailField)
    except User.DoesNotExist:
        return {'code': 'account/usernotfound', 'values': [emailField]}, 404

    code = Code.objects.create(text=helpers.makeCode(), created_user=user, type=1)

    config = home.helpers.getConfig(request)
    config['code'] = code.text
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['user_first_name'] = user.first_name

    helpers.sendmail(subject='Reset password',
                     html_content=render_to_string('account/templates/resetpassword.email.htm', config),
                     text_content=render_to_string('account/templates/resetpassword.email.txt', config),
                     to_email=[emailField])

    return {'code': 'ok', 'data': [emailField]}


# Reset password
@json_view
def actionResetpassword(request):
    """Reset password action"""

    if request.user.is_authenticated():
        return {'code': 'noaccess'}, 404

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User, Code

    validateResult, validateCode = validateResetpassword(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        codeField = json_data['code']
        codeField = codeField.lower()
    except:
        codeField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = ''

    try:
        code = Code.objects.get(text=codeField)
    except Code.DoesNotExist:
        return {'code': 'account/codenotfound', 'values': [codeField]}, 404

    user = User.objects.get(pk=code.created_user.id)

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        updateFromJsonObject(user, json_data)
        user.save()
        auth.login(request, user)
        Code.objects.filter(created_user=user).delete()

        return {'code': 'ok', 'data': [user.getUserData()]}
    else:
        auth.logout(request)
        return {'code': 'account/notactive'}, 404
