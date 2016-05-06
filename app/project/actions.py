# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from project import settings
import resource
import validator


@json_view
def get_list(request):
    """List data"""

    if settings.ENV == 'production':
        try:
            data, code, items = resource.get_list(request)
        except:
            return {'code': 'project/get_list/fail'}, 404
    else:
        data, code, items = resource.get_list(request)

    return data, code


@json_view
def get_list_by_tag(request, tag_text):
    """List data"""

    if settings.ENV == 'production':
        try:
            data, code, items = resource.get_list_by_tag(request, tag_text)
        except:
            return {'code': 'project/get_list_by_tag/fail'}, 404
    else:
        data, code, items = resource.get_list_by_tag(request, tag_text)

    return data, code


@json_view
def get_search(request, search_text):
    """Search data"""

    if settings.ENV == 'production':
        try:
            data, code, items = resource.get_search(request, search_text)
        except:
            return {'code': 'project/get_search/fail'}, 404
    else:
        data, code, items = resource.get_search(request, search_text)

    return data, code


@json_view
def get_item_by_name(request, project_name):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item_by_name(request, project_name)
        except:
            return {'code': 'project/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item_by_name(request, project_name)
    return data, code

@json_view
def get_item(request, project_id):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item(request, project_id)
        except:
            return {'code': 'project/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item(request, project_id)
    return data, code


@json_view
def update(request, project_id):
    """Update record"""

    data, code, valid = validator.update(request, project_id)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, item = resource.update(request, project_id)
            except:
                return {'code': 'project/update/fail'}, 404
        else:
            data, code, item = resource.update(request, project_id)

    return data, code


@json_view
def create(request):
    """Create record"""

    data, code, valid = validator.create(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, item = resource.create(request)
            except:
                return {'code': 'project/create/fail'}, 404
        else:
            data, code, item = resource.create(request)

    return data, code


@json_view
def delete(request, project_id):
    """Delete record"""

    data, code, valid = validator.delete(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code = resource.delete(request, project_id)
            except:
                return {'code': 'project/delete/fail'}, 404
        else:
            data, code = resource.delete(request, project_id)

    return data, code
