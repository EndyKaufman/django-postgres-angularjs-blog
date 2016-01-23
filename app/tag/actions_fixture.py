# -*- coding: utf-8 -*-

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.conf import settings
# from django.contrib import auth
# from django.contrib.auth.models import User
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError

import json
from jsonview.decorators import json_view

# list
@json_view
def getList(request):
    """List data"""

    try:
        with open('app/tag/fixtures/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '{}'
    data = json.loads(content)

    return {'code': 'ok', 'data': data}
