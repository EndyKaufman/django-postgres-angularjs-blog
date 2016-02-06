# -*- coding: utf-8 -*-

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
        content = '[]'
    data = json.loads(content)

    return {'code': 'ok', 'data': data}
