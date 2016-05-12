# -*- coding: utf-8 -*-
from project import helpers
from project import settings
from django.template.loader import render_to_string


def get_fields():
    return ['email', 'username', 'message']

def send(request):
    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields(), '')

    data['email'] = data['email'].lower()

    config = {}
    config['SHORT_SITE_NAME'] = settings.SHORT_SITE_NAME
    config['email'] = data['email']
    config['username'] = data['username']
    config['message'] = data['message']

    helpers.send_mail(subject='Message from contact form',
                      html_content=render_to_string('contact/templates/message.email.htm', config),
                      text_content=render_to_string('contact/templates/message.email.txt', config))

    return {'code': 'ok', 'data': [data['email']]}, 200, data['email']
