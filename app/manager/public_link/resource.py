# -*- coding: utf-8 -*-
from project import helpers
from ..models import PublicLink


def get_fields():
    return [f.name for f in PublicLink._meta.get_fields()]


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    item, created = PublicLink.objects.get_or_create(src=data['src'])

    if created:
        helpers.json_to_objects(item, data)
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, public_link_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = PublicLink.objects.get(pk=public_link_id)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_id]}, 404, False

    helpers.json_to_objects(item, data)
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, public_link_id):
    """Update record"""
    try:
        item = PublicLink.objects.get(pk=public_link_id)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, public_link_id):
    try:
        item = PublicLink.objects.get(pk=public_link_id)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_src(request, public_link_src):
    try:
        item = PublicLink.objects.get(src=public_link_src)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_src]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    items = PublicLink.objects.all().order_by('position').all()
    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = PublicLink.objects.filter(
            helpers.get_searching_all_fields_qs(PublicLink, search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
