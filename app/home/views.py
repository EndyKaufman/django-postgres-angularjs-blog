# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
import json
import helpers
import helpers_fixtures

# Create your views here.
def index(request):
    """Home page maker"""
    if settings.USE_FIXTURE:
        return render(request, 'home/templates/index.htm', {
            'config': json.dumps(helpers_fixtures.getConfig(request), sort_keys=True, indent=4),
            'settings': settings
        })
    else:
        return render(request, 'home/templates/index.htm', {
            'config': json.dumps(helpers.getConfig(request), sort_keys=True, indent=4),
            'settings': settings
        })
