# -*- coding: utf-8 -*-

from app.home import helpers
from jsonview.decorators import json_view
from project import helpers
import helpers as meta_tag_helpers


# list
@json_view
def getList(request):
    """List data"""

    data = meta_tag_helpers.getList()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, id):
    """Item data"""

    data = meta_tag_helpers.getItem(id)

    if not data:
        return {'code': 'meta_tag/not_found', 'values': [id]}, 404
    else:
        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# update
@json_view
def actionUpdate(request, id):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'content', 'attributes', 'position'])

    if json_data['position'] == '':
        json_data['position'] = None;

    data = meta_tag_helpers.getItemByName(json_data['name'])

    if (data is not False) and (int(data[0].id) != int(id)):
        return {'code': 'meta_tag/exists', 'values': [json_data['name']]}, 404

    data = meta_tag_helpers.getItem(id)

    if not data:
        return {'code': 'meta_tag/not_found', 'values': [id]}, 404
    else:
        try:
            data[0].name = json_data['name']
            data[0].content = json_data['content']
            data[0].attributes = json_data['attributes']
            data[0].position = json_data['position']
            data[0].save()
        except:
            return {'code': 'meta_tag/update/fail'}, 404
        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'content', 'attributes', 'position'])

    if json_data['position'] == '':
        json_data['position'] = None;

    json_data['created_user'] = user

    data = meta_tag_helpers.getItemByName(json_data['name'])

    if data is not False:
        return {'code': 'meta_tag/exists', 'values': [json_data['name']]}, 404

    data = meta_tag_helpers.create(json_data)

    if not data:
        return {'code': 'meta_tag/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# delete
@json_view
def actionDelete(request, id):
    """Delete record"""
    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    data = meta_tag_helpers.getItem(id)

    if not data:
        return {'code': 'meta_tag/not_found', 'values': [id]}, 404
    else:
        try:
            data[0].delete()
        except:
            return {'code': 'meta_tag/delete/fail'}, 404
        return {'code': 'ok'}
