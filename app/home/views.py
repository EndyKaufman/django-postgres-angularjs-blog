# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from app.manager.meta_tag import helpers as meta_tag_helpers
from app.manager.properties import helpers as properties_helpers


# Create your views here.
@ensure_csrf_cookie
def index(request):
    """Home page maker"""
    if settings.USE_MOCK:
        from helpers_mock import getConfig
    else:
        from helpers import getConfig

    config = getConfig(request)
    config['properties'] = properties_helpers.getListOfNames(
        ['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME', 'SITE_LOGO'])

    meta_tag_list = meta_tag_helpers.getList()

    properties_list = properties_helpers.getListOfNames(
        ['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME', 'SITE_LOGO', 'HOME_HEADER_BOTTOM_HTML',
         'HOME_BODY_TOP_HTML', 'HOME_BODY_BOTTOM_HTML'])

    return render(request, 'home/templates/%s/index.htm' % settings.THEME, {
        'config': json.dumps(config, sort_keys=True, indent=4),
        'settings': settings,
        'meta_tag_list': meta_tag_list,
        'properties_list': properties_list
    })
