# -*- coding: utf-8 -*-
from project import helpers
from ..models import MetaTag


def get_fields():
    return [f.name for f in MetaTag._meta.get_fields()]


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    item, created = MetaTag.objects.get_or_create(name=data['name'])

    if created:
        helpers.json_to_objects(item, data)
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, meta_tag_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = MetaTag.objects.get(pk=meta_tag_id)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_id]}, 404, False

    helpers.json_to_objects(item, data)
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, meta_tag_id):
    """Update record"""

    try:
        item = MetaTag.objects.get(pk=meta_tag_id)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, meta_tag_id):
    try:
        item = MetaTag.objects.get(pk=meta_tag_id)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_name(request, meta_tag_name):
    try:
        item = MetaTag.objects.get(name=meta_tag_name)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_name]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    items = MetaTag.objects.all().order_by('position').all()
    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_list_as_objects():
    try:
        items = MetaTag.objects.all().order_by('position').all()
    except MetaTag.DoesNotExist:
        items = []
    return items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = MetaTag.objects.filter(
            helpers.get_searching_all_fields_qs(MetaTag, search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
