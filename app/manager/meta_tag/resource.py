# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['name', 'content', 'attributes', 'position']


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.manager.models import MetaTag

    item, created = MetaTag.objects.get_or_create(name=data['name'], content=data['content'],
                                                  attributes=data['attributes'],
                                                  position=data['position'], created_user=user)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, meta_tag_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(pk=meta_tag_id)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_id]}, 404, False

    if data['name'] is not None:
        item.name = data['name']
    if data['content'] is not None:
        item.content = data['content']
    if data['attributes'] is not None:
        item.attributes = data['attributes'],
    if data['position'] is not None:
        item.position = data['position']

    item.created_user = user
    item.save()
    
    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, meta_tag_id):
    """Update record"""

    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(pk=meta_tag_id)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, meta_tag_id):
    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(pk=meta_tag_id)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_name(request, meta_tag_name):
    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(name=meta_tag_name)
    except MetaTag.DoesNotExist:
        return {'code': 'meta_tag/not_found', 'values': [meta_tag_name]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from app.manager.models import MetaTag

    items = MetaTag.objects.all().order_by('position').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.manager.models import MetaTag

        items = MetaTag.objects.filter(
            Q(name__icontains=search_text) |
            Q(content__icontains=search_text) |
            Q(attributes__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
