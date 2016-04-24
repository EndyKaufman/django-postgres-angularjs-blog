# -*- coding: utf-8 -*-

from app.home import helpers
from jsonview.decorators import json_view
from project import helpers
import helpers as properties_helpers


# list
@json_view
def getList(request):
    """List data"""

    data = properties_helpers.getList()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, id):
    """Item data"""

    data = properties_helpers.getItem(id)

    if not data:
        return {'code': 'properties/notfound', 'values': [id]}, 404
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

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'value'])

    data = properties_helpers.getItemByName(json_data['name'])

    if (data is not False) and (int(data[0].id) != int(id)):
        return {'code': 'properties/exists', 'values': [json_data['name']]}, 404

    data = properties_helpers.getItem(id)

    if not data:
        return {'code': 'properties/notfound', 'values': [id]}, 404
    else:
        try:
            data[0].name = json_data['name']
            data[0].content = json_data['value']
            data[0].save()
        except:
            return {'code': 'properties/update/fail'}, 404
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

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'value'])

    json_data['created_user'] = user

    data = properties_helpers.getItemByName(json_data['name'])

    if data is not False:
        return {'code': 'properties/exists', 'values': [json_data['name']]}, 404

    data = properties_helpers.create(json_data)

    if not data:
        return {'code': 'properties/create/fail'}, 404

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

    data = properties_helpers.getItem(id)

    if not data:
        return {'code': 'properties/notfound', 'values': [id]}, 404
    else:
        try:
            data[0].delete()
        except:
            return {'code': 'properties/delete/fail'}, 404
        return {'code': 'ok'}
