# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from project import helpers
import helpers as public_link_helpers


# list
@json_view
def getList(request):
    """List data"""

    data = public_link_helpers.getList()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, data)}


# item
@json_view
def getItem(request, id):
    """Item data"""

    data = public_link_helpers.getItem(id)

    if not data:
        return {'code': 'public_link/not_found', 'values': [id]}, 404
    else:
        return {'code': 'ok', 'data': helpers.objects_to_json(request, data)}


# update
@json_view
def actionUpdate(request, id):
    """Update record"""

    json_data = helpers.get_json(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    json_data = helpers.set_null_values_If_not_exist(json_data,
                                                     ['src', 'title', 'icon', 'in_header', 'in_footer', 'in_contact',
                                                 'position'])
    if json_data['position'] == '':
        json_data['position'] = None;

    data = public_link_helpers.getItemBySrc(json_data['src'])

    if (data is not False) and (int(data[0].id) != int(id)):
        return {'code': 'public_link/exists', 'values': [json_data['src']]}, 404

    data = public_link_helpers.getItem(id)

    if not data:
        return {'code': 'public_link/not_found', 'values': [id]}, 404
    else:
        try:
            data[0].src = json_data['src']
            data[0].title = json_data['title']
            data[0].icon = json_data['icon']
            data[0].position = json_data['position']
            data[0].in_header = json_data['in_header']
            data[0].in_footer = json_data['in_footer']
            data[0].in_contact = json_data['in_contact']
            data[0].save()
        except:
            return {'code': 'public_link/update/fail'}, 404
        return {'code': 'ok', 'data': helpers.objects_to_json(request, data)}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = helpers.get_json(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    json_data = helpers.set_null_values_If_not_exist(json_data,
                                                     ['src', 'title', 'icon', 'in_header', 'in_footer', 'in_contact',
                                                 'position'])
    if json_data['position'] == '':
        json_data['position'] = None;

    json_data['created_user'] = user

    data = public_link_helpers.getItemBySrc(json_data['src'])

    if data is not False:
        return {'code': 'public_link/exists', 'values': [json_data['src']]}, 404

    data = public_link_helpers.create(json_data)

    if not data:
        return {'code': 'public_link/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.objects_to_json(request, data)}


# delete
@json_view
def actionDelete(request, id):
    """Delete record"""
    json_data = helpers.get_json(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    data = public_link_helpers.getItem(id)

    if not data:
        return {'code': 'public_link/not_found', 'values': [id]}, 404
    else:
        try:
            data[0].delete()
        except:
            return {'code': 'public_link/delete/fail'}, 404
        return {'code': 'ok'}
