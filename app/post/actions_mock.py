# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers


# list
@json_view
def getList(request):
    """List data"""

    try:
        with open('mock/post/list.json') as f:
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

    if search_text == '*':
        return getList(request)
    else:
        try:
            with open('mock/post/list.json') as f:
                content = f.read()
                f.close()
        except IOError:
            content = '[]'
        data = json.loads(content)

        return {'code': 'ok', 'data': data}


# search by tag
@json_view
def getListByTag(request, tag_text):
    """List data by tag"""

    try:
        with open('mock/post/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    return {'code': 'ok', 'data': data}


# item
@json_view
def getItem(request, post_name):
    """Item data"""

    try:
        with open('mock/post/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    item = False
    for record in data:
        if record['name'] == post_name:
            item = record

    if item is False:
        return {'code': 'post/notfound', 'values': [post_name]}, 404

    return {'code': 'ok', 'data': [item]}


# update
@json_view
def actionUpdate(request, post_id):
    """Update record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.post.models import Post

    validateResult, validateCode = Post.validateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    return {'code': 'ok', 'data': [json_data], 'reload_source': {'tag': True, 'image': True}}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.post.models import Post

    validateResult, validateCode = Post.validateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    if len(json_data['tags']) > 0:
        json_data['tags'][0]['id'] = 101
    if len(json_data['images']) > 0:
        json_data['images'][0]['id'] = 101
    return {'code': 'ok', 'data': [json_data], 'reload_source': {'tag': True, 'image': True}}


# delete
@json_view
def actionDelete(request, post_id):
    """Delete record"""

    return {'code': 'ok'}