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
            return {'code': 'user_app/get_list/fail'}, 404
    else:
        data, code, items = resource.get_list(request)

    return data, code


@json_view
def get_search(request, search_text):
    """Search data"""

    if settings.ENV == 'production':
        try:
            data, code, items = resource.get_search(request, search_text)
        except:
            return {'code': 'user_app/get_search/fail'}, 404
    else:
        data, code, items = resource.get_search(request, search_text)

    return data, code


@json_view
def get_item_by_client_id(request, user_app_client_id):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item_by_client_id(request, user_app_client_id)
        except:
            return {'code': 'user_app/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item_by_client_id(request, user_app_client_id)
    return data, code


@json_view
def get_item(request, user_app_id):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item(request, user_app_id)
        except:
            return {'code': 'user_app/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item(request, user_app_id)
    return data, code


@json_view
def update(request, user_app_id):
    """Update record"""

    data, code, valid = validator.update(request, user_app_id)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, item = resource.update(request, user_app_id)
            except:
                return {'code': 'user_app/update/fail'}, 404
        else:
            data, code, item = resource.update(request, user_app_id)

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
                return {'code': 'user_app/create/fail'}, 404
        else:
            data, code, item = resource.create(request)

    return data, code


@json_view
def delete(request, user_app_id):
    """Delete record"""

    data, code, valid = validator.delete(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code = resource.delete(request, user_app_id)
            except:
                return {'code': 'user_app/delete/fail'}, 404
        else:
            data, code = resource.delete(request, user_app_id)

    return data, code
