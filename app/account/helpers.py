# -*- coding: utf-8 -*-

from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def getUserByCode(code_text):
    from app.account.models import User, Code

    try:
        code = Code.objects.get(text=code_text)
    except Code.DoesNotExist:
        code = False

    if code:
        try:
            user = User.objects.get(pk=code.created_user.id)
        except User.DoesNotExist:
            user = False
        return user, code
    else:
        return False, False


def getUserByEmail(email):
    from app.account.models import User

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = False

    return user


def updateFromJsonObject(user, jsonObject):
    try:
        emailField = jsonObject['email']
        emailField = emailField.lower()
    except:
        emailField = ''
    try:
        passwordField = jsonObject['password']
    except KeyError:
        passwordField = ''
    try:
        usernameField = jsonObject['username']
    except KeyError:
        usernameField = ''
    try:
        first_nameField = jsonObject['firstname']
    except KeyError:
        first_nameField = ''
    try:
        last_nameField = jsonObject['lastname']
    except KeyError:
        last_nameField = ''

    if emailField != '':
        user.email = emailField

    if passwordField != '':
        user.set_password(passwordField)

    if first_nameField != '':
        user.first_name = first_nameField

    if last_nameField != '':
        user.last_name = last_nameField

    return {'code': 'ok'}, 200


def validateProfileUpdate(jsonObject):
    try:
        emailField = jsonObject['email']
        emailField = emailField.lower()
    except:
        emailField = ''

    if emailField == '':
        return {'code': 'account/not_email'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    return {'code': 'ok'}, 200


def validateLogin(jsonObject):
    try:
        emailField = jsonObject['email']
        emailField = emailField.lower()
    except:
        emailField = ''
    try:
        passwordField = jsonObject['password']
    except KeyError:
        passwordField = ''

    if emailField == '':
        return {'code': 'account/not_email'}, 404

    if passwordField == '':
        return {'code': 'account/no_password'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    return {'code': 'ok'}, 200


def validateRecovery(jsonObject):
    try:
        emailField = jsonObject['email']
        emailField = emailField.lower()
    except:
        emailField = ''

    if emailField == '':
        return {'code': 'account/not_email'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404

    return {'code': 'ok'}, 200


def validateResetpassword(jsonObject):
    try:
        codeField = jsonObject['code']
        codeField = codeField.lower()
    except:
        codeField = ''
    try:
        passwordField = jsonObject['password']
    except KeyError:
        passwordField = ''

    if codeField == '':
        return {'code': 'account/no_code'}, 404

    if passwordField == '':
        return {'code': 'account/no_password'}, 404

    return {'code': 'ok'}, 200
