# -*- coding: utf-8 -*-
from project import helpers
from project import settings
from django.template.loader import render_to_string
from ..manager.properties import resource as properties_resource
from django.utils.translation import ugettext, get_language


def get_fields():
    return ['email', 'username', 'message']


def send(request):
    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields(), '')

    data['email'] = data['email'].lower()

    config = {}
    config['email'] = data['email']
    config['username'] = data['username']
    config['message'] = data['message']
    config['properties'] = properties_resource.get_list_of_names(['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME',
                                                                  'SITE_LOGO'])

    helpers.send_mail(subject=ugettext('Message from contact form'),
                      html_content=render_to_string(
                          'contact/templates/%s/%s/message.email.htm' % (settings.THEME, get_language()), config),
                      text_content=render_to_string(
                          'contact/templates/%s/%s/message.email.txt' % (settings.THEME, get_language()), config),
                      config=config)

    return {'code': 'ok', 'data': [data['email']]}, 200, data['email']
