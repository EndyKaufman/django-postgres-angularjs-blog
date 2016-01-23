# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
import json
import config


# Create your views here.
def index(request):
    """Home page maker"""

    return render(request, 'home/templates/index.htm', {
        'config': json.dumps(config.get(request), sort_keys=True, indent=4),
        'settings': settings
    })
