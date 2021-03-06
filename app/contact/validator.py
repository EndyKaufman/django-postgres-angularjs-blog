# -*- coding: utf-8 -*-
from project import helpers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import resource

def send(request):
    """Send message"""

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())
    data['email'] = data['email'].lower()

    if data['email'] == '':
        return {'code': 'contact/not_email'}, 404, False
    if data['username'] == '':
        return {'code': 'contact/not_username'}, 404, False
    if data['message'] == '':
        return {'code': 'contact/not_message'}, 404, False

    # Validate values of fields
    try:
        validate_email(data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    return {'code': 'ok'}, 200, True
