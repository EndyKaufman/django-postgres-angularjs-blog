# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['url', 'content']


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.manager.models import HtmlCache

    item, created = HtmlCache.objects.get_or_create(url=data['url'], content=data['content'], created_user=user)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def create_by_url(url, content):
    from app.manager.models import HtmlCache
    item, created = HtmlCache.objects.get_or_create(url=url, content=content)
    return item


def update_by_url(url, content):
    """Update record"""

    item = get_item_by_url(url)
    if item:
        item.content = content
        if item.content == '':
            item.content = None

        item.save()
    else:
        create_by_url(url, content)
    return item


def update(request, html_cache_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.manager.models import HtmlCache

    try:
        item = HtmlCache.objects.get(pk=html_cache_id)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_id]}, 404, False

    if data['url'] is not None:
        item.url = data['url']
    if data['content'] is not None:
        item.content = data['content']

    item.created_user = user
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, html_cache_id):
    """Update record"""

    from app.manager.models import HtmlCache

    try:
        item = HtmlCache.objects.get(pk=html_cache_id)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, html_cache_id):
    from app.manager.models import HtmlCache

    try:
        item = HtmlCache.objects.get(pk=html_cache_id)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_url(html_cache_url):
    from app.manager.models import HtmlCache

    try:
        return HtmlCache.objects.get(url=html_cache_url)
    except HtmlCache.DoesNotExist:
        return False


def get_item_by_url(request, html_cache_url):
    from app.manager.models import HtmlCache

    try:
        item = HtmlCache.objects.get(url=html_cache_url)
    except HtmlCache.DoesNotExist:
        return {'code': 'html_cache/not_found', 'values': [html_cache_url]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from app.manager.models import HtmlCache

    items = HtmlCache.objects.all().order_by('position').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.manager.models import HtmlCache

        items = HtmlCache.objects.filter(
            Q(url__icontains=search_text) |
            Q(content__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
