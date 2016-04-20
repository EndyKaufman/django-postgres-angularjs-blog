# -*- coding: utf-8 -*-

from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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
        return {'code': 'account/noemail'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrongemail'}, 404

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
        return {'code': 'account/noemail'}, 404

    if passwordField == '':
        return {'code': 'account/nopassword'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrongemail'}, 404

    return {'code': 'ok'}, 200


def validateRecovery(jsonObject):
    try:
        emailField = jsonObject['email']
        emailField = emailField.lower()
    except:
        emailField = ''

    if emailField == '':
        return {'code': 'account/noemail'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrongemail'}, 404

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
        return {'code': 'account/nocode'}, 404

    if passwordField == '':
        return {'code': 'account/nopassword'}, 404

    return {'code': 'ok'}, 200
