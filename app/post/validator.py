# -*- coding: utf-8 -*-
from project import helpers
import resource


def create(request):
    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'title', 'description'])

    if json_data['name'] is None:
        return {'code': 'post/no_name'}, 404
    if json_data['title'] is None:
        return {'code': 'post/no_title'}, 404
    if json_data['description'] is None:
        return {'code': 'post/no_description'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_name(request, json_data['name'])

    if item is not False:
        return {'code': 'post/exists', 'values': [json_data['name']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request, post_id):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'title', 'description'])

    if json_data['name'] is None:
        return {'code': 'post/no_name'}, 404
    if json_data['title'] is None:
        return {'code': 'post/no_title'}, 404
    if json_data['description'] is None:
        return {'code': 'post/no_description'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_name(request, json_data['name'])

    if (item is not False) and (int(item.id) != int(post_id)):
        return {'code': 'post/exists', 'values': [json_data['text']]}, 404, False

    return {'code': 'ok'}, 200, True


def delete(request):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True
