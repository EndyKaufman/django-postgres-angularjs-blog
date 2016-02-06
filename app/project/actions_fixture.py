# -*- coding: utf-8 -*-

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.conf import settings
# from django.contrib import auth
# from app.account.models import User
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError

import json
from jsonview.decorators import json_view


# list
@json_view
def getList(request):
    """List data"""

    try:
        with open('app/project/fixtures/list.json') as f:
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
        with open('app/project/fixtures/list.json') as f:
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
        with open('app/project/fixtures/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    return {'code': 'ok', 'data': data}


# item
@json_view
def getItem(request, project_name):
    """Item data"""

    try:
        with open('app/project/fixtures/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    data = json.loads(content)

    item = {}
    for record in data:
        if record['name'] == project_name:
            item = record

    return {'code': 'ok', 'data': [item]}


# update
@json_view
def actionUpdate(request, project_id):
    """Update record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.project.models import Project

    validateResult, validateCode = Project.validateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    return {'code': 'ok', 'data': [json_data]}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.project.models import Project

    validateResult, validateCode = Project.validateJsonObject(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    json_data['tags'][0]['id'] = 101
    json_data['images'][0]['id'] = 101
    return {'code': 'ok', 'data': [json_data]}


# delete
@json_view
def actionDelete(request, project_id):
    """Delete record"""

    return {'code': 'ok'}
