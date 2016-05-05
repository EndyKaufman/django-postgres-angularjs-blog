# -*- coding: utf-8 -*-
from project import helpers
from project import settings
from django.template.loader import render_to_string


def send(request):
    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, ['email', 'username', 'message'], '')

    json_data['email'] = json_data['email'].lower()

    config = {}
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['email'] = json_data['email']
    config['username'] = json_data['username']
    config['message'] = json_data['message']

    helpers.sendmail(subject='Message from contact form',
                     html_content=render_to_string('contact/templates/message.email.htm', config),
                     text_content=render_to_string('contact/templates/message.email.txt', config))

    return {'code': 'ok', 'data': [json_data['email']]}, 200, json_data['email']
