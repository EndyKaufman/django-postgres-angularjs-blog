# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers
from app import home
from django.conf import settings
from django.template.loader import render_to_string


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
    except:
        emailField = ''

    if emailField == '':
        return {'code': 'account/noemail'}, 404

    try:
        with open('mock/account/users.json') as f:
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
        if emailField == settings.EMAIL_HOST_USER.lower():
            user = records[1]
            user['id'] = 7
            user['email'] = emailField
        else:
            return {'code': 'account/usernotfound', 'values': [emailField]}, 404

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
    except:
        emailField = ''

    if emailField == '':
        return {'code': 'account/noemail'}, 404

    try:
        with open('mock/account/users.json') as f:
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
    except:
        emailField = ''
    try:
        passwordField = json_data['password']
    except KeyError:
        passwordField = ''

    try:
        with open('mock/account/users.json') as f:
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
        if emailField == settings.EMAIL_HOST_USER.lower():
            user = records[1]
            user['id'] = 7
            user['email'] = emailField
        else:
            return {'code': 'account/usernotfound', 'values': [emailField]}, 404
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


# Recovery
@json_view
def actionRecovery(request):
    """Recovery action"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    validateResult, validateCode = User.validateRecoveryJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except:
        emailField = ''

    try:
        with open('mock/account/users.json') as f:
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
        if emailField == settings.EMAIL_HOST_USER.lower():
            user = records[1]
            user['id'] = 7
            user['email'] = emailField
        else:
            return {'code': 'account/usernotfound', 'values': [emailField]}, 404

    config = home.helpers.getConfig(request)
    config['code'] = helpers.makeCode()
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['user_first_name'] = user['firstname']

    helpers.sendmail(subject='Reset password',
                     html_content=render_to_string('account/templates/resetpassword.email.htm', config),
                     text_content=render_to_string('account/templates/resetpassword.email.txt', config))

    return {'code': 'ok', 'data': [emailField]}


# Reset password
@json_view
def actionResetpassword(request):
    """Reset password action"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    validateResult, validateCode = User.validateResetpasswordJsonObject(json_data)

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
        with open('mock/account/users.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    user = records[1]
    user['id'] = 7
    user['email'] = settings.EMAIL_HOST_USER

    return {'code': 'ok', 'data': [user]}
