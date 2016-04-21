# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from project import helpers
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string


# send message
@json_view
def actionSend(request):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data, ['email', 'username', 'message'])
    json_data['email'] = json_data['email'].lower()

    if json_data['email'] == '':
        return {'code': 'contact/noemail'}, 404
    if json_data['username'] == '':
        return {'code': 'contact/nousername'}, 404
    if json_data['message'] == '':
        return {'code': 'contact/nomessage'}, 404

    # Validate values of fields
    try:
        validate_email(json_data['email'])
    except ValidationError:
        return {'code': 'account/wrongemail'}, 404

    config = {}
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['email'] = json_data['email']
    config['username'] = json_data['username']
    config['message'] = json_data['message']

    helpers.sendmail(subject='Message from contact form',
                     html_content=render_to_string('contact/templates/message.email.htm', config),
                     text_content=render_to_string('contact/templates/message.email.txt', config))

    return {'code': 'ok', 'data': [json_data['email']]}
