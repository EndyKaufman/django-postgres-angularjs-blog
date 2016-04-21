# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from app.manager.meta_tag import helpers as meta_tag_helpers


# Create your views here.
@ensure_csrf_cookie
def index(request):
    """Home page maker"""
    if settings.USE_MOCK:
        from helpers_mock import getConfig
    else:
        from helpers import getConfig

    return render(request, 'home/templates/%s/index.htm' % settings.THEME, {
        'config': json.dumps(getConfig(request), sort_keys=True, indent=4),
        'settings': settings,
        'meta_tag_list': meta_tag_helpers.getList()
    })
