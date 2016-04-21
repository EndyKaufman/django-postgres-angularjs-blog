# -*- coding: utf-8 -*-

from app.home import helpers
from jsonview.decorators import json_view
from project import helpers
import helpers as public_link_helpers


# list
@json_view
def getList(request):
    """List data"""

    data = public_link_helpers.getList()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, id):
    """Item data"""

    data = public_link_helpers.getItem(id)

    if not data:
        return {'code': 'public_link/notfound', 'values': [id]}, 404
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

    json_data = helpers.setNullValuesIfNotExist(json_data,
                                                ['src', 'title', 'icon', 'in_header', 'in_footer', 'in_contact'])

    data = public_link_helpers.getItemByName(json_data['src'])

    if (data is not False) and (int(data[0].id) != int(id)):
        return {'code': 'public_link/exists', 'values': [json_data['src']]}, 404

    data = public_link_helpers.getItem(id)

    if not data:
        return {'code': 'public_link/notfound', 'values': [id]}, 404
    else:
        try:
            data[0].src = json_data['src']
            data[0].title = json_data['title']
            data[0].icon = json_data['icon']
            data[0].in_header = json_data['in_header']
            data[0].in_footer = json_data['in_footer']
            data[0].in_contact = json_data['in_contact']
            data[0].save()
        except:
            return {'code': 'public_link/update/fail'}, 404
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

    data = public_link_helpers.getItemByName(json_data['name'])

    if data is not False:
        return {'code': 'public_link/exists', 'values': [json_data['name']]}, 404

    data = public_link_helpers.create(json_data)

    if not data:
        return {'code': 'public_link/create/fail'}, 404

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

    data = public_link_helpers.getItem(id)

    if not data:
        return {'code': 'public_link/notfound', 'values': [id]}, 404
    else:
        try:
            data[0].delete()
        except:
            return {'code': 'public_link/delete/fail'}, 404
        return {'code': 'ok'}
