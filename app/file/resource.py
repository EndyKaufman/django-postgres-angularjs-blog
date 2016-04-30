# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def create(request):
    json_data = request.POST

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, ['comment'])

    if request.FILES and request.FILES.get('file'):
        if user.is_superuser:
            url = helpers.saveFile(False,
                                   request.FILES.get('file'))
        else:
            url = helpers.saveFile(str(user.id),
                                   request.FILES.get('file'))
    else:
        url = ''

    from app.file.models import File

    item, created = File.objects.get_or_create(src=url)
    if created:
        item.comment = json_data['comment']
        item.created_user = user
        item.save()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def update(request, file_id):
    """Update record"""

    json_data = helpers.getJson(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, ['comment'])

    from app.file.models import File

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404, False

    item.comment = json_data['comment']
    item.save()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def delete(request, file_id):
    """Update record"""

    from app.file.models import File

    try:
        item = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404

    helpers.removeFile(item.src)
    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, file_id):
    from app.file.models import File

    try:
        data = [File.objects.get(pk=file_id)]
    except File.DoesNotExist:
        return {'code': 'file/not_found', 'values': [file_id]}, 404, False

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}, 200, data[0]


def get_list(request):
    from app.file.models import File

    data = File.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}, 200, data


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.file.models import File

        data = File.objects.filter(
            Q(comment__icontains=search_text) |
            Q(src__icontains=search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}, 200, data
