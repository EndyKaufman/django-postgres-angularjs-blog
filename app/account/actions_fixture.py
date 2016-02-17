# -*- coding: utf-8 -*-

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

    from app.account.models import User

    validateResult, validateCode = User.validateProfileUpdateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except KeyError:
        emailField = ''

    if emailField == '':
        return {'code': 'account/noemail'}, 404

    try:
        with open('app/account/fixtures/users.json') as f:
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
                username = ''

            if firstname != '':
                user['firstname'] = firstname

            if lastname != '':
                user['lastname'] = lastname

            if username != '':
                user['username'] = username

    if user == False:
        return {'code': 'account/usernofound', 'values': [emailField]}, 404

    return {'code': 'ok', 'data': [user]}


# reg
@json_view
def actionReg(request):
    """Update record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    validateResult, validateCode = User.validateProfileUpdateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except KeyError:
        emailField = ''

    if emailField == '':
        return {'code': 'account/noemail'}, 404

    try:
        with open('app/account/fixtures/users.json') as f:
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
                username = ''

            if firstname != '':
                user['firstname'] = firstname

            if lastname != '':
                user['lastname'] = lastname

            if username != '':
                user['username'] = username

    if user != False:
        return {'code': 'account/exists', 'values': [emailField]}, 404
    else:
        user = records[1]
        user['id'] = 7
        user['email'] = emailField

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

    from app.account.models import User

    validateResult, validateCode = User.validateLoginJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except KeyError:
        emailField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = ''

    try:
        with open('app/account/fixtures/users.json') as f:
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
        return {'code': 'account/usernofound', 'values': [emailField]}, 404
    return {'code': 'ok', 'data': [user]}


# Logout
@json_view
def actionDelete(request):
    """Delete record"""

    # auth.logout(request)
    return {'code': 'ok'}


# Logout
@json_view
def actionLogout(request):
    """Logout action"""

    # auth.logout(request)
    return {'code': 'ok'}
