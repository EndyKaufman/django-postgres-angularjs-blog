# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['text', 'description']


def get_item_by_text(request, text):
    from app.tag.models import Tag
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

    from app.tag.models import Tag

    item, created = Tag.objects.get_or_create(text=data['text'])
    if created:
        if data['description'] is not None:
            item.description = data['description']
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, tag_id):
    """Update record"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.tag.models import Tag

    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404, False

    if data['text'] is not None:
        item.text = data['text']
    if data['description'] is not None:
        item.description = data['description']
        
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, tag_id):
    """Update record"""

    from app.tag.models import Tag

    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, tag_id):
    from app.tag.models import Tag

    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from app.tag.models import Tag

    items = Tag.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.tag.models import Tag

        items = Tag.objects.filter(
            Q(text_icontains=search_text) |
            Q(description__icontains=search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
