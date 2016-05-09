# -*- coding: utf-8 -*-
from project import helpers
import resource


def create(request):
    json_data = helpers.get_json(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.set_null_values_If_not_exist(json_data, resource.get_fields())

    if json_data['name'] is None:
        return {'code': 'project/no_name'}, 404
    if json_data['title'] is None:
        return {'code': 'project/no_title'}, 404
    if json_data['description'] is None:
        return {'code': 'project/no_description'}, 404

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_name(request, json_data['name'])

    if item is not False:
        return {'code': 'project/exists', 'values': [json_data['name']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request, project_id):
    """Update record"""

    json_data = helpers.get_json(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    json_data = helpers.set_null_values_If_not_exist(json_data, resource.get_fields())

    if json_data['name'] is None:
        return {'code': 'project/no_name'}, 404
    if json_data['title'] is None:
        return {'code': 'project/no_title'}, 404
    if json_data['description'] is None:
        return {'code': 'project/no_description'}, 404

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_name(request, json_data['name'])

    if (item is not False) and (int(item.id) != int(project_id)):
        return {'code': 'project/exists', 'values': [json_data['text']]}, 404, False

    return {'code': 'ok'}, 200, True


def delete(request):
    """Update record"""

    json_data = helpers.get_json(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True
