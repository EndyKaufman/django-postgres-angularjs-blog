# -*- coding: utf-8 -*-
from project import helpers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import resource

def send(request):
    """Send message"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data, resource.get_fields())
    json_data['email'] = json_data['email'].lower()

    if json_data['email'] == '':
        return {'code': 'contact/not_email'}, 404, False
    if json_data['username'] == '':
        return {'code': 'contact/nousername'}, 404, False
    if json_data['message'] == '':
        return {'code': 'contact/nomessage'}, 404, False

    # Validate values of fields
    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrong_email'}, 404, False

    return {'code': 'ok'}, 200, True
