# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers
from django.db.models import Q


# list
@json_view
def getList(request):
    """List data"""

    from app.manager.models import MetaTag

    data = MetaTag.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, id):
    """Item data"""

    from app.manager.models import MetaTag

    try:
        data = [MetaTag.objects.get(pk=id)]
    except MetaTag.DoesNotExist:
        return {'code': 'metatag/notfound', 'values': [id]}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# update
@json_view
def actionUpdate(request, id):
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

    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(name=json_data['name'])
    except MetaTag.DoesNotExist:
        item = False

    if (item is not False) and (int(item.id) != int(id)):
        return {'code': 'metatag/exists', 'values': [json_data['name'], item.id]}, 404

    try:
        item = MetaTag.objects.get(pk=id)
    except MetaTag.DoesNotExist:
        return {'code': 'metatag/notfound', 'values': [id]}, 404

    # try:
    item.name = json_data['name']
    item.content = json_data['content']
    item.attributes = json_data['attributes']
    item.save()
    # except:
    #    return {'code': 'metatag/update/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}


# create
@json_view
def actionCreate(request):
    """Create record"""

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

    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(name=json_data['name'])
    except MetaTag.DoesNotExist:
        item = False

    if item is not False:
        return {'code': 'metatag/exists', 'values': [json_data['name']]}, 404

    # try:
    item = MetaTag.objects.create(name=json_data['name'], content=json_data['content'],
                                  attributes=json_data['attributes'])
    # except:
    #     return {'code': 'metatag/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}


# delete
@json_view
def actionDelete(request, id):
    """Delete record"""

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

    from app.manager.models import MetaTag

    try:
        item = MetaTag.objects.get(pk=id)
    except item.DoesNotExist:
        return {'code': 'metatag/notfound', 'values': [id]}, 404

    try:
        item.delete()
    except:
        return {'code': 'metatag/delete/fail'}, 404

    return {'code': 'ok'}
