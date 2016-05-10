# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['src', 'title', 'icon', 'in_header', 'in_footer', 'position', 'in_contact']


def create(request):
    json_data = helpers.get_json(request)

    user = helpers.get_user(request)

    json_data = helpers.set_null_values_If_not_exist(json_data, get_fields())

    from app.manager.models import PublicLink

    item, created = PublicLink.objects.get_or_create(src=json_data['src'], title=json_data['title'],
                                                     icon=json_data['icon'], in_header=json_data['in_header'],
                                                     in_footer=json_data['in_footer'],
                                                     position=json_data['position'],
                                                     in_contact=json_data['in_contact'],
                                                     created_user=user)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, public_link_id):
    """Update record"""

    json_data = helpers.get_json(request)

    user = helpers.get_user(request)

    json_data = helpers.set_null_values_If_not_exist(json_data, get_fields())

    from app.manager.models import PublicLink

    try:
        item = PublicLink.objects.get(pk=public_link_id)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_id]}, 404, False

    item.src = json_data['src']
    item.title = json_data['title']
    item.icon = json_data['icon']
    item.in_header = json_data['in_header']
    item.in_footer = json_data['in_footer']
    item.position = json_data['position']
    item.in_contact = json_data['in_contact']
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, public_link_id):
    """Update record"""

    from app.manager.models import PublicLink

    try:
        item = PublicLink.objects.get(pk=public_link_id)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, public_link_id):
    from app.manager.models import PublicLink

    try:
        item = PublicLink.objects.get(pk=public_link_id)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_src(request, public_link_src):
    from app.manager.models import PublicLink

    try:
        item = PublicLink.objects.get(src=public_link_src)
    except PublicLink.DoesNotExist:
        return {'code': 'public_link/not_found', 'values': [public_link_src]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from app.manager.models import PublicLink

    items = PublicLink.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.manager.models import PublicLink

        items = PublicLink.objects.filter(
            Q(src__icontains=search_text) |
            Q(title__icontains=search_text) |
            Q(icon__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
