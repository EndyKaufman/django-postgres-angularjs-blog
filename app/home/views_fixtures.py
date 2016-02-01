# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
import json
import config_fixtures


# Create your views here.
def index(request):
    """Home page maker"""

    return render(request, 'home/templates/index.htm', {
        'config': json.dumps(config_fixtures.get(request), sort_keys=True, indent=4),
        'settings': settings
    })
