# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['comment']

def create(request):
    """Create record"""

    json_data = request.POST

    user = helpers.get_user(request)

    json_data = helpers.set_null_values_if_not_exist(json_data, get_fields())

    if request.FILES and request.FILES.get('file'):
        if user.is_superuser:
            url = helpers.save_file(False,
                                    request.FILES.get('file'))
        else:
            url = helpers.save_file(str(user.id),
                                    request.FILES.get('file'))
    else:
        url = ''

    from app.file.models import File

    item, created = File.objects.get_or_create(src=url)
    if created:
        item.comment = json_data['comment']
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, file_id):
    """Update record"""

    json_data = helpers.get_json(request)

    json_data = helpers.set_null_values_if_not_exist(json_data, get_fields())

    from app.file.models import File

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404, False

    item.comment = json_data['comment']
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, file_id):
    """Update record"""

    from app.file.models import File

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404

    helpers.remove_file(item.src)
    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, file_id):
    from app.file.models import File

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from app.file.models import File

    items = File.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.file.models import File

        items = File.objects.filter(
            Q(comment__icontains=search_text) |
            Q(src__icontains=search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
