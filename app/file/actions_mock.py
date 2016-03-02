# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers


# list
@json_view
def getList(request):
    """List data"""

    try:
        with open('mock/file/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    return {'code': 'ok', 'data': data}


# search
@json_view
def getSearch(request, search_text):
    """Search data"""

    try:
        with open('mock/file/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    return {'code': 'ok', 'data': data}


# item
@json_view
def getItem(request, file_id):
    """Item data"""

    try:
        with open('mock/file/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    item = {}
    for record in data:
        if record['id'] == file_id:
            item = record

    if item is False:
        return {'code': 'file/notfound', 'values': [file_id]}, 404

    return {'code': 'ok', 'data': data}


# update
@json_view
def actionUpdate(request, file_id):
    """Update record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    try:
        comment = json_data['comment']
    except:
        comment = None

    return {'code': 'ok', 'data': [json_data]}


# create
@json_view
def actionCreate(request):
    """Create record"""

    if request.method != 'POST':
        return {'code': 'nodata'}, 404

    if request.FILES and request.FILES.get('file'):
        url = helpers.saveFile(False, request.FILES.get('file'), 'test.file')
    else:
        url = ''

    try:
        comment = request.POST['comment']
    except:
        comment = None

    file = {'id': 777, 'src': url, 'comment': comment}

    return {'code': 'ok', 'data': [file]}


# delete
@json_view
def actionDelete(request, file_id):
    """Delete record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    try:
        helpers.removeFile('test.file')
    except:
        return {'code': 'file/fail/delete'}, 404

    return {'code': 'ok'}
