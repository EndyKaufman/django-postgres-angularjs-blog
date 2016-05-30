# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q
from models import File

def get_fields():
    return [f.name for f in File._meta.get_fields()]


def create(request):
    """Create record"""

    data = request.POST

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    if request.FILES and request.FILES.get('file'):
        if user.is_superuser:
            url = helpers.save_file(False,
                                    request.FILES.get('file'))
        else:
            url = helpers.save_file(str(user.id),
                                    request.FILES.get('file'))
    else:
        url = ''

    item, created = File.objects.get_or_create(src=url)
    if created:
        helpers.json_to_objects(item, data)
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, file_id):
    """Update record"""

    data = request.DATA

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404, False

    helpers.json_to_objects(item, data)
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, file_id):
    """Update record"""

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404

    helpers.remove_file(item.src)
    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, file_id):
    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    items = File.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = File.objects.filter(
            helpers.get_searching_all_fields_qs(File, search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
