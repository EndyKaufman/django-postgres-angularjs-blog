# -*- coding: utf-8 -*-
from project import helpers
import resource


def create(request):
    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['src'] is None:
        return {'code': 'public_link/no_src'}, 404, False

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_src(request, data['src'])

    if item is not False:
        return {'code': 'public_link/exists', 'values': [data['src']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request, public_link_id):
    """Update record"""

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['src'] is None:
        return {'code': 'public_link/no_src'}, 404, False

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_src(request, data['src'])

    if (item is not False) and (int(item.id) != int(public_link_id)):
        return {'code': 'public_link/exists', 'values': [data['text']]}, 404, False

    return {'code': 'ok'}, 200, True


def delete(request):
    """Update record"""

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True
