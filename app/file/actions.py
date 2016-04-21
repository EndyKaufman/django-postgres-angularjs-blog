# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers
from django.db.models import Q


# list
@json_view
def getList(request):
    """List data"""

    from app.file.models import File

    data = File.objects.all().order_by('created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# search
@json_view
def getSearch(request, search_text):
    """Search data"""

    if search_text == 'all':
        return getList(request)
    else:
        from app.file.models import File

        data = File.objects.filter(
            Q(comment__icontains=search_text) |
            Q(src__icontains=search_text)
        ).order_by('created').all()

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, file_id):
    """Item data"""

    from app.file.models import File

    try:
        data = [File.objects.get(pk=file_id)]
    except File.DoesNotExist:
        return {'code': 'file/notfound', 'values': [file_id]}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# update
@json_view
def actionUpdate(request, file_id):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

    json_data = helpers.setNullValuesIfNotExist(json_data, ['comment'])

    from app.file.models import File

    try:
        file = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/notfound', 'values': [file_id]}, 404

    try:
        file.comment = json_data['comment']
        file.save()
    except:
        return {'code': 'file/update/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([file])}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = request.POST

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

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

    try:
        file, created = File.objects.get_or_create(src=url)
        if created:
            file.comment = json_data['comment']
            file.created_user = user
            file.save()
    except:
        return {'code': 'file/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([file])}


# delete
@json_view
def actionDelete(request, file_id):
    """Delete record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'nodata'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404
    if user is None:
        return {'code': 'account/younotactive'}, 404

    from app.file.models import File

    try:
        file = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/notfound', 'values': [file_id]}, 404

    try:
        helpers.removeFile(file.src)
        file.delete()
    except:
        return {'code': 'file/delete/fail'}, 404

    return {'code': 'ok'}
