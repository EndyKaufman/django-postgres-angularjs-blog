# -*- coding: utf-8 -*-
from project import helpers
from models import Tag


def get_fields():
    return [f.name for f in Tag._meta.get_fields()]


def get_item_by_text(request, text):
    try:
        item = Tag.objects.get(text=text)
    except Tag.DoesNotExist:
        item = False
    return item


def create(request):
    """Create record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    item, created = Tag.objects.get_or_create(text=data['text'])
    if created:
        helpers.json_to_objects(item, data)
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, tag_id):
    """Update record"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404, False

    helpers.json_to_objects(item, data)
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, tag_id):
    """Update record"""
    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, tag_id):
    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    items = Tag.objects.all().order_by('created').all()
    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = Tag.objects.filter(
            helpers.get_searching_all_fields_qs(Tag, search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
