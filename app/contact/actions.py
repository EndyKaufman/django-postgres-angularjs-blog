# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from django.conf import settings
import validator
import resource


@json_view
def send(request):
    """Send message"""

    data, code, valid = validator.send(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, email = resource.send(request)
            except:
                return {'code': 'contact/send/fail'}, 404
        else:
            data, code, user = resource.send(request)

    return data, code
