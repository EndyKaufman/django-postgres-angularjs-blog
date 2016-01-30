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


# update
@json_view
def actionUpdate(request):
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
        return {'code': 'auth/noemail'}, 404

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
        if record['userData']['email'] == emailField:
            user = record
            try:
                firstname = json_data['firstname']
            except KeyError:
                firstname = False
            if firstname != False:
                user['userData']['firstname'] = firstname

            try:
                lastname = json_data['lastname']
            except KeyError:
                lastname = False
            if lastname != False:
                user['userData']['lastname'] = lastname

            try:
                username = json_data['username']
            except KeyError:
                username = False
            if username != False:
                user['userData']['username'] = username

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
        return {'code': 'auth/noemail'}, 404
    try:
        passwordField = json_data['password']
    except KeyError:
        return {'code': 'auth/nopassword'}, 404

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

    '''
    # Try auth
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return {'code': 'auth/usernofound', 'values': [email]}, 404

    user = auth.authenticate(username=user.username, password=password)

    if user is None:
        return { 'code': 'auth/wrongpassword' % email}, 404

    if user.is_active:
        user.backend = 'django.contrib.auth.backends.ModelBackend'    
        auth.login(request, user)
        return { 'code': 'ok', 'user': { 
            'id': user.id, 
            'username': user.username, 
            'first_name': user.first_name, 
            'last_name': user.last_name, 
            'email': user.email, 
            'is_active': user.is_active, 
            'is_staff': user.is_staff, 
            'is_superuser': user.is_superuser
            }
        }
    else:
        auth.logout(request)
        return { 'code': 'auth/notactive'}, 404
    '''
    try:
        with open('app/myauth/fixtures/users.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    user = False

    for record in records:
        if record['userData']['email'] == emailField:
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
