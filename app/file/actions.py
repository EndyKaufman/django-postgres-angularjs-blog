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

    if not request.user.is_authenticated() or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return {'code': 'account/younotactive'}, 404

    try:
        comment = json_data['comment']
    except:
        comment = None

    from app.file.models import File

    try:
        file = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/notfound', 'values': [file_id]}, 404

    # try:
    file.comment = comment
    file.save()
    # except:
    #    return {'code': 'file/update/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([file])}


# create
@json_view
def actionCreate(request):
    """Create record"""

    if not request.user.is_authenticated() or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404

    if request.method != 'POST':
        return {'code': 'nodata'}, 404

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return {'code': 'account/younotactive'}, 404

    if request.FILES and request.FILES.get('file'):
        if user.is_superuser:
            url = helpers.saveFile(False,
                                   request.FILES.get('file'))
        else:
            url = helpers.saveFile(str(user.id),
                                   request.FILES.get('file'))
    else:
        url = ''

    try:
        comment = request.POST['comment']
    except:
        comment = None

    from app.file.models import File

    # try:
    file, created = File.objects.get_or_create(src=url)
    if created:
        file.comment = comment
        file.created_user = user
        file.save()
    # except:
    #    return {'code': 'file/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([file])}


# delete
@json_view
def actionDelete(request, file_id):
    """Delete record"""

    if not request.user.is_authenticated() or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.file.models import File

    try:
        file = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return {'code': 'file/notfound', 'values': [file_id]}, 404

    try:
        helpers.removeFile(file.src)
        file.delete()
    except:
        return {'code': 'file/fail/delete'}, 404

    return {'code': 'ok'}
