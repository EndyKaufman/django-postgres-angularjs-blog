# -*- coding: utf-8 -*-
from project import helpers
from ..models import HtmlCache


def get_fields():
    return [f.name for f in HtmlCache._meta.get_fields()]


def create_by_url(url, content):
    item, created = HtmlCache.objects.get_or_create(url=url, content=content)
    return item


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    item, created = HtmlCache.objects.get_or_create(url=data['url'])

    if created:
        helpers.json_to_objects(item, data)
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update_by_url(url, content):
    """Update record"""
    item = get_object_by_url(url)
    if item:
        item.content = content
        if item.content == '':
            item.content = None
        item.save()
    else:
        item = create_by_url(url, content)
    return item


def update(request, html_cache_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = HtmlCache.objects.get(pk=html_cache_id)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_id]}, 404, False

    helpers.json_to_objects(item, data)
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, html_cache_id):
    """Update record"""

    try:
        item = HtmlCache.objects.get(pk=html_cache_id)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, html_cache_id):
    try:
        item = HtmlCache.objects.get(pk=html_cache_id)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_object_by_url(html_cache_url):
    try:
        return HtmlCache.objects.get(url=html_cache_url)
    except HtmlCache.DoesNotExist:
        return False


def get_item_by_url(request, html_cache_url):
    try:
        item = HtmlCache.objects.get(url=html_cache_url)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_url]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    items = HtmlCache.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = HtmlCache.objects.filter(
            helpers.get_searching_all_fields_qs(HtmlCache, search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
