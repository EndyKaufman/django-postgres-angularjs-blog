# -*- coding: utf-8 -*-

import json
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

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    try:
        emailField = json_data['email']
        emailField = emailField.lower()
    except:
        emailField = ''

    try:
        usernameField = json_data['username']
    except:
        usernameField = ''

    try:
        messageField = json_data['message']
    except:
        messageField = ''

    if emailField == '':
        return {'code': 'contact/noemail'}, 404
    if usernameField == '':
        return {'code': 'contact/nousername'}, 404
    if messageField == '':
        return {'code': 'contact/nomessage'}, 404

    # Validate values of fields
    try:
        validate_email(emailField)
    except ValidationError:
        return {'code': 'account/wrongemail'}, 404

    config = {}
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['email'] = emailField
    config['username'] = usernameField
    config['message'] = messageField

    helpers.sendmail(subject='Message from contact form',
                     html_content=render_to_string('contact/templates/message.email.htm', config),
                     text_content=render_to_string('contact/templates/message.email.txt', config))

    return {'code': 'ok', 'data': [emailField]}
