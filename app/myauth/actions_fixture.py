# -*- coding: utf-8 -*-

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.conf import settings
# from django.contrib import auth
# from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from jsonview.decorators import json_view
from django.views.decorators.csrf import csrf_exempt


# update
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

    if emailField == '':
        return {'code': 'auth/noemail'}, 404

    emailField = emailField.lower()

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'auth/wrongemail'}, 404

    try:
        with open('app/myauth/fixtures/users.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    user = False

    for record in records:
        if record['email'] == emailField:
            user = record
            try:
                firstname = json_data['firstname']
            except KeyError:
                firstname = ''
            try:
                lastname = json_data['lastname']
            except KeyError:
                lastname = ''
            try:
                username = json_data['username']
            except KeyError:
                username = emailField[:30]

            user['firstname'] = firstname
            user['lastname'] = lastname
            user['username'] = username

    if user == False:
        return {'code': 'auth/usernofound', 'values': [emailField]}, 404

    return {'code': 'ok', 'data': [user]}


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

    try:
        with open('app/myauth/fixtures/users.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    user = False

    for record in records:
        if record['email'] == emailField:
            user = record

    if user == False:
        return {'code': 'auth/usernofound', 'values': [emailField]}, 404
    return {'code': 'ok', 'data': [user]}


# Logout
@json_view
def actionLogout(request):
    """Logout action"""

    # auth.logout(request)
    return {'code': 'ok'}
