# -*- coding: utf-8 -*-

import json

def getUserData(request):
    config = {}

    try:
        with open('app/myauth/fixtures/guest.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    config = json.loads(content)

    return config
