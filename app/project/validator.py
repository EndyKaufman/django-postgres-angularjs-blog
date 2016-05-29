# -*- coding: utf-8 -*-
from project import helpers
import resource
from django.utils.translation import get_language


def create(request):
    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['name'] is None:
        return {'code': 'project/no_name'}, 404, False
    if data['title_%s' % get_language()] is None:
        return {'code': 'project/no_title'}, 404, False
    if data['description_%s' % get_language()] is None:
        return {'code': 'project/no_description'}, 404, False

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_name(request, data['name'])

    if item is not False:
        return {'code': 'project/exists', 'values': [data['name']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request, project_id):
    """Update record"""

    data = request.DATA

    if data is False:
        return {'code': 'no_data'}, 404, False

    data = helpers.set_null_values_if_not_exist(data, resource.get_fields())

    if data['name'] is None:
        return {'code': 'project/no_name'}, 404, False
    if data['title_%s' % get_language()] is None:
        return {'code': 'project/no_title'}, 404, False
    if data['description_%s' % get_language()] is None:
        return {'code': 'project/no_description'}, 404, False

    user = helpers.get_user(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    data, code, item = resource.get_item_by_name(request, data['name'])

    if (item is not False) and (int(item.id) != int(project_id)):
        return {'code': 'project/exists', 'values': [data['text']]}, 404, False

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
