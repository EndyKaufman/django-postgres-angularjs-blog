# -*- coding: utf-8 -*-
from project import helpers, settings
from ..models import Properties
from django.core.files import File
import os
from django.utils.translation import get_language


def get_fields():
    return [f.name for f in Properties._meta.get_fields()]


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    item, created = Properties.objects.get_or_create(name=data['name'])

    if created:
        helpers.json_to_objects(item, data)
        item.created_user = user
        item.only_update = 0
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def apply_on_site(request):
    props = get_list_as_objects()
    for prop in props:
        if prop.name == 'FAVICON':
            from favicon.models import Favicon
            item, created = Favicon.objects.get_or_create(title='FAVICON')
            file_name = getattr(prop, 'value_%s' % get_language(), None)
            item.faviconImage.save(
                os.path.basename(file_name),
                File(open(os.path.join(settings.MEDIA_ROOT, file_name)))
            )
            item.save()
    return {'code': 'ok'}, 200, True


def update(request, properties_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = Properties.objects.get(pk=properties_id)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_id]}, 404, False

    helpers.json_to_objects(item, data)
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, properties_id):
    """Update record"""
    try:
        item = Properties.objects.get(pk=properties_id)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, properties_id):
    try:
        item = Properties.objects.get(pk=properties_id)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_name(request, properties_name):
    try:
        item = Properties.objects.get(name=properties_name)
    except Properties.DoesNotExist:
        return {'code': 'properties/not_found', 'values': [properties_name]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list_of_names(names):
    items = get_list_as_objects()
    list_of_names = helpers.set_null_values_if_not_exist({}, names, '')
    if len(names) > 0:
        for item in items:
            for name in names:
                if item.name == name:
                    list_of_names[name] = getattr(item, 'value_%s' % get_language(), None)
    else:
        for item in items:
            list_of_names[item.name] = item['value_%s' % get_language()]
    return list_of_names


def get_list(request):
    items = Properties.objects.all().order_by('created').all()
    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_list_as_objects():
    try:
        items = Properties.objects.all().order_by('created').all()
    except Properties.DoesNotExist:
        items = []
    return items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = Properties.objects.filter(
            helpers.get_searching_all_fields_qs(Properties, search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
