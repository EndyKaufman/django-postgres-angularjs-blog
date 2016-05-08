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

    json_data = helpers.getJson(request)

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, get_fields())

    from app.tag.models import Tag

    item, created = Tag.objects.get_or_create(text=json_data['text'])
    if created:
        item.description = json_data['description']
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def update(request, tag_id):
    """Update record"""

    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, get_fields())

    from app.tag.models import Tag

    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return {'code': 'tag/not_found', 'values': [tag_id]}, 404, False

    item.text = json_data['text']
    item.description = json_data['description']
    item.save()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


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

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def get_list(request):
    from app.tag.models import Tag

    items = Tag.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.tag.models import Tag

        items = Tag.objects.filter(
            Q(text_icontains=search_text) |
            Q(description__icontains=search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items
