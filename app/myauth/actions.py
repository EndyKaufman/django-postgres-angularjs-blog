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


# Login
@json_view
def postLogin(request):
    """Login action"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    # Validate fields
    try:
        email = json_data['email']
    except KeyError:
        return {'code': 'account/noemail'}, 404
    try:
        password = json_data['password']
    except KeyError:
        return {'code': 'account/nopassword'}, 404

    if email == '':
        return {'code': 'account/noemail'}, 404

    if password == '':
        return {'code': 'account/nopassword'}, 404

    email = email.lower()

    # Validate values of fields
    try:
        validate_email(email)
    except ValidationError:
        return {'code': 'account/wrongemail'}, 404

    '''
    # Try auth
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return {'code': 'account/usernofound', 'values': [email]}, 404

    user = auth.authenticate(username=user.username, password=password)

    if user is None:
        return { 'code': 'account/wrongpassword' % email}, 404

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
        return { 'code': 'account/notactive'}, 404
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
        if record['userData']['userEmail'] == email:
            user = record

    if user == False:
        return {'code': 'account/usernofound', 'values': [email]}, 404

    return {'code': 'ok', 'data': user}


# Logout
@json_view
def postLogout(request):
    """Logout action"""

    # auth.logout(request)
    return {'code': 'ok'}
