# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['name', 'value', 'comment']


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.manager.models import Properties

    item, created = Properties.objects.get_or_create(name=data['name'], value=data['value'],
                                                     comment=data['comment'],
                                                     created_user=user, only_update=0)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, properties_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.manager.models import Properties

    try:
        item = Properties.objects.get(pk=properties_id)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_id]}, 404, False

    item.name = data['name']
    item.value = data['value']
    item.comment = data['comment']
    item.created_user = user
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, properties_id):
    """Update record"""

    from app.manager.models import Properties

    try:
        item = Properties.objects.get(pk=properties_id)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, properties_id):
    from app.manager.models import Properties

    try:
        item = Properties.objects.get(pk=properties_id)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_name(request, properties_name):
    from app.manager.models import Properties

    try:
        item = Properties.objects.get(name=properties_name)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_name]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list_of_names(request, names):
    data, code, items = get_list(request)
    list_of_names = helpers.set_null_values_if_not_exist({}, names, '')
    if len(names) > 0:
        for item in items:
            for name in names:
                if item.name == name:
                    list_of_names[name] = item.value
    else:
        for item in items:
            list_of_names[item.name] = item.value
    return list_of_names


def get_list(request):
    from app.manager.models import Properties

    items = Properties.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.manager.models import Properties

        items = Properties.objects.filter(
            Q(name__icontains=search_text) |
            Q(content__icontains=search_text) |
            Q(attributes__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
