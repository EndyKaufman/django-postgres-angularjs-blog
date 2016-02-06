# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib import auth
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from jsonview.decorators import json_view
import helpers
from django.views.decorators.csrf import csrf_exempt


# update profile
@json_view
def actionProfileUpdate(request):
    """Update record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    # Validate fields
    try:
        emailField = json_data['email']
    except KeyError:
        emailField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = False
    try:
        first_name = json_data['firstname']
    except KeyError:
        first_name = ''
    try:
        last_name = json_data['lastname']
    except KeyError:
        last_name = ''

    if emailField == '':
        return {'code': 'auth/noemail'}, 404

    emailField = emailField.lower()

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'auth/wrongemail'}, 404

    from django.contrib.auth.models import User

    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return {'code': 'auth/usernofound', 'values': [emailField]}, 404

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    try:
        user.email = emailField
        user.first_name = first_name
        user.last_name = last_name
        if passwordField != False:
            user.set_password(passwordField)
        user.save()
    except:
        return {'code': 'auth/profile/fail/update'}, 404

    return {'code': 'ok', 'data': [helpers.getUserData(user)]}


# Login
@json_view
def actionLogin(request):
    """Login action"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    # Validate fields
    try:
        emailField = json_data['email']
    except KeyError:
        emailField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = ''

    if emailField == '':
        return {'code': 'auth/noemail'}, 404

    if passwordField == '':
        return {'code': 'auth/nopassword'}, 404

    emailField = emailField.lower()

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'auth/wrongemail'}, 404

    # Try auth

    from django.contrib.auth.models import User

    try:
        user = User.objects.get(email=emailField)
    except User.DoesNotExist:
        return {'code': 'auth/usernofound', 'values': [emailField]}, 404

    user = auth.authenticate(username=user.username, password=passwordField)

    if user is None:
        return {'code': 'auth/wrongpassword'}, 404

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        return {'code': 'ok', 'data': [helpers.getUserData(user)]}
    else:
        auth.logout(request)
        return {'code': 'auth/notactive'}, 404


# Logout
@json_view
def actionLogout(request):
    """Logout action"""

    auth.logout(request)
    return {'code': 'ok'}
