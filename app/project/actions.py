# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers
from helpers import updateFromJsonObject, validate
from django.db.models import Q


# list
@json_view
def getList(request):
    """List data"""

    from app.project.models import Project

    data = Project.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# search
@json_view
def getSearch(request, search_text):
    """Search data"""
    if search_text == 'all':
        return getList(request)
    else:
        from app.project.models import Project

        data = Project.objects.filter(
            Q(title__icontains=search_text) |
            Q(name__icontains=search_text) |
            Q(description__icontains=search_text) |
            Q(url__icontains=search_text) |
            Q(text__icontains=search_text) |
            Q(html__icontains=search_text) |
            Q(markdown__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# search by tag
@json_view
def getListByTag(request, tag_text):
    """List data by tag"""

    from app.project.models import Project

    data = Project.objects.filter(tags__text=tag_text).order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, project_name):
    """Item data"""

    from app.project.models import Project

    try:
        data = [Project.objects.get(name=project_name)]
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_name]}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# update
@json_view
def actionUpdate(request, project_id):
    """Update record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    from app.project.models import Project

    validateResult, validateCode = validate(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        project = Project.objects.get(name=json_data['name'])
    except Project.DoesNotExist:
        project = False

    if (project is not False) and (int(project.id) != int(project_id)):
        return {'code': 'project/exists', 'values': [json_data['name'], project.id]}, 404

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404

    # try:
    updateResult, updateCode = updateFromJsonObject(project, json_data, user)
    if updateCode != 200:
        return updateResult, updateCode
    project.save()
    # except:
    #    return {'code': 'project/update/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([project]), 'reload_source': updateResult['reload_source']}


# create
@json_view
def actionCreate(request):
    """Create record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    from app.project.models import Project

    validateResult, validateCode = validate(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        project = Project.objects.get(name=json_data['name'])
    except Project.DoesNotExist:
        project = False

    if project is not False:
        return {'code': 'project/exists', 'values': [json_data['name']]}, 404

    project = Project.objects.create(name=json_data['name'], type=1, created_user=user)

    # try:
    createResult, createCode = updateFromJsonObject(project, json_data, user)
    if createCode != 200:
        return createResult, createCode
    project.save()
    # except:
    #     return {'code': 'project/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([project]), 'reload_source': createResult['reload_source']}


# delete
@json_view
def actionDelete(request, project_id):
    """Delete record"""

    json_data = helpers.getJson(request)

    if json_data is False:
        return {'code': 'no_data'}, 404

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404
    if user is None:
        return {'code': 'account/not_active'}, 404

    from app.project.models import Project

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404

    try:
        project.delete()
    except:
        return {'code': 'project/delete/fail'}, 404

    return {'code': 'ok'}
