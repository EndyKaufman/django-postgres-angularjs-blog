# -*- coding: utf-8 -*-
from project import helpers
import resource


def create(request):
    json_data = request.POST

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    item = resource.get_tag_by_text(json_data['text'])

    if item is not False:
        return {'code': 'tag/exists', 'values': [json_data['text']]}, 404, False

    return {'code': 'ok'}, 200, True


def update(request, tag_id):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    item = resource.get_tag_by_text(json_data['text'])

    if (item is not False) and (int(item.id) != int(tag_id)):
        return {'code': 'tag/exists', 'values': [json_data['text']]}, 404, False

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
