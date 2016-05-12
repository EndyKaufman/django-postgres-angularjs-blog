# -*- coding: utf-8 -*-
from project import helpers
import resource
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def create(request):
    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['password'] is None:
        return {'code': 'account/no_password'}, 404, False

    if data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    data['email'] = data['email'].lower()

    try:
        validate_email(data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = resource.get_item_by_email(request, data['email'])

    if user:
        return {'code': 'account/exists', 'values': [data['email']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request):
    """Update record"""

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    data['email'] = data['email'].lower()

    try:
        validate_email(data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = helpers.get_user(request)

    if not user:
        return {'code': 'no_access'}, 404, False

    return {'code': 'ok'}, 200, True


def delete(request):
    """Update record"""

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.get_user(request)

    if not user:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True


def login(request):
    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['password'] is None:
        return {'code': 'account/no_password'}, 404, False

    if data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    data['email'] = data['email'].lower()

    try:
        validate_email(data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = resource.get_item_by_email(request, data['email'])

    if not user:
        return {'code': 'account/user_not_found', 'values': [data['email']]}, 404, False

    return {'code': 'ok'}, 200, True


def logout(request):
    """Update record"""

    user = helpers.get_user(request)

    if not user:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True


def recovery(request):
    """Recovery action"""

    if request.user.is_authenticated():
        return {'code': 'no_access'}, 404, False

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['email'] is None:
        return {'code': 'account/not_email'}, 404, False

    data['email'] = data['email'].lower()

    try:
        validate_email(data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    user = resource.get_item_by_email(request, data['email'])

    if not user:
        return {'code': 'account/user_not_found', 'values': [data['email']]}, 404, False

    return {'code': 'ok'}, 200, True


def reset_password(request):
    """Reset password action"""

    if request.user.is_authenticated():
        return {'code': 'no_access'}, 404, False

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['code'] is None:
        return {'code': 'account/no_code'}, 404, False

    data['code'] = data['code'].lower()

    if data['password'] is None:
        return {'code': 'account/no_password'}, 404, False

    code = resource.get_code(request, data['code'])

    if not code:
        return {'code': 'account/code_not_found', 'values': [data['code']]}, 404, False

    return {'code': 'ok'}, 200, True

