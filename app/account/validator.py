# -*- coding: utf-8 -*-
from project import helpers
import resource
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def create(request):
    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email', 'password'])

    if json_data['password'] is None:
        return {'code': 'account/no_password'}, 404, False

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = resource.get_item_by_email(json_data['email'])

    if user:
        return {'code': 'account/exists', 'values': [json_data['email']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email', 'password', 'username', 'firstname', 'lastname'])

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404, False

    return {'code': 'ok'}, 200, True


def delete(request):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True


def login(request):
    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email', 'password'])

    if json_data['password'] is None:
        return {'code': 'account/no_password'}, 404, False

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = resource.get_item_by_email(json_data['email'])

    if not user:
        return {'code': 'account/user_not_found', 'values': [json_data['email']]}, 404, False

    return {'code': 'ok'}, 200, True


def logout(request):
    """Update record"""

    user = helpers.getUser(request)

    if not user:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True


def recovery(request):
    """Recovery action"""

    if request.user.is_authenticated():
        return {'code': 'no_access'}, 404, False

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['email'])

    if json_data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    json_data['email'] = json_data['email'].lower()

    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = resource.get_item_by_email(json_data['email'])

    if not user:
        return {'code': 'account/user_not_found', 'values': [json_data['email']]}, 404, False

    return {'code': 'ok'}, 200, True


def reset_password(request):
    """Reset password action"""

    if request.user.is_authenticated():
        return {'code': 'no_access'}, 404, False

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['code', 'password'])

    if json_data['code'] is None:
        return {'code': 'account/no_code'}, 404, False

    json_data['code'] = json_data['code'].lower()

    if json_data['password'] is None:
        return {'code': 'account/no_password'}, 404, False

    code = resource.get_code(json_data['code'])

    if not code:
        return {'code': 'account/code_not_found', 'values': [json_data['code']]}, 404, False

    return {'code': 'ok'}, 200, True

