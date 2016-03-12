# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import helpers
import helpers_mock


# Create your views here.
@ensure_csrf_cookie
def index(request):
    """Home page maker"""
    if settings.USE_MOCK:
        return render(request, 'home/templates/%s/index.htm' % settings.THEME, {
            'config': json.dumps(helpers_mock.getConfig(request), sort_keys=True, indent=4),
            'settings': settings
        })
    else:
        return render(request, 'home/templates/%s/index.htm' % settings.THEME, {
            'config': json.dumps(helpers.getConfig(request), sort_keys=True, indent=4),
            'settings': settings
        })
