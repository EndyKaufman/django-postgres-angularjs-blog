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
        return {'code': 'metatag/notfound', 'values': [id]}, 404
    else:
        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# update
@json_view
def actionUpdate(request, id):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'content', 'attributes'])

    data = meta_tag_helpers.getItemByName(json_data['name'])

    if (data is not False) and (int(data[0].id) != int(id)):
        return {'code': 'metatag/exists', 'values': [json_data['name']]}, 404

    data = meta_tag_helpers.getItem(id)

    if not data:
        return {'code': 'metatag/notfound', 'values': [id]}, 404
    else:
        try:
            data[0].name = json_data['name']
            data[0].content = json_data['content']
            data[0].attributes = json_data['attributes']
            data[0].save()
        except:
            return {'code': 'metatag/update/fail'}, 404
        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'content', 'attributes'])

    json_data['created_user'] = user

    data = meta_tag_helpers.getItemByName(json_data['name'])

    if data is not False:
        return {'code': 'metatag/exists', 'values': [json_data['name']]}, 404

    data = meta_tag_helpers.create(json_data)

    if not data:
        return {'code': 'metatag/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# delete
@json_view
def actionDelete(request, id):
    """Delete record"""
    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

    data = meta_tag_helpers.getItem(id)

    if not data:
        return {'code': 'metatag/notfound', 'values': [id]}, 404
    else:
        try:
            data[0].delete()
        except:
            return {'code': 'metatag/delete/fail'}, 404
        return {'code': 'ok'}
