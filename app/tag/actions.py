# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from project import helpers
import helpers as tag_helpers


# list
@json_view
def getList(request):
    """List data"""

    data = tag_helpers.getList()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, id):
    """Item data"""

    data = tag_helpers.getItem(id)

    if not data:
        return {'code': 'tag/not_found', 'values': [id]}, 404
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

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['text', 'description'])

    data = tag_helpers.getItemByText(json_data['text'])

    if (data is not False) and (int(data[0].id) != int(id)):
        return {'code': 'tag/exists', 'values': [json_data['text']]}, 404

    data = tag_helpers.getItem(id)

    if not data:
        return {'code': 'tag/not_found', 'values': [id]}, 404
    else:
        try:
            data[0].text = json_data['text']
            data[0].description = json_data['description']
            data[0].save()
        except:
            return {'code': 'tag/update/fail'}, 404
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

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['text', 'description'])

    json_data['created_user'] = user

    data = tag_helpers.getItemByText(json_data['text'])

    if data is not False:
        return {'code': 'tag/exists', 'values': [json_data['text']]}, 404

    data = tag_helpers.create(json_data)

    if not data:
        return {'code': 'tag/create/fail'}, 404

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

    data = tag_helpers.getItem(id)

    if not data:
        return {'code': 'tag/not_found', 'values': [id]}, 404
    else:
        try:
            data[0].delete()
        except:
            return {'code': 'tag/delete/fail'}, 404
        return {'code': 'ok'}
