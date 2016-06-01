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
            return {'code': 'properties/get_list/fail'}, 404
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
            return {'code': 'properties/get_search/fail'}, 404
    else:
        data, code, items = resource.get_search(request, search_text)

    return data, code


@json_view
def get_item_by_name(request, properties_name):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item_by_name(request, properties_name)
        except:
            return {'code': 'properties/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item_by_name(request, properties_name)
    return data, code


@json_view
def get_item(request, properties_id):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item(request, properties_id)
        except:
            return {'code': 'properties/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item(request, properties_id)
    return data, code


@json_view
def update(request, properties_id):
    """Update record"""

    data, code, valid = validator.update(request, properties_id)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, item = resource.update(request, properties_id)
            except:
                return {'code': 'properties/update/fail'}, 404
        else:
            data, code, item = resource.update(request, properties_id)

    return data, code


@json_view
def apply_on_site(request):
    """Update record"""

    data, code, valid = validator.apply_on_site(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, item = resource.apply_on_site(request)
            except:
                return {'code': 'properties/apply_on_site/fail'}, 404
        else:
            data, code, item = resource.apply_on_site(request)

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
                return {'code': 'properties/create/fail'}, 404
        else:
            data, code, item = resource.create(request)

    return data, code


@json_view
def delete(request, properties_id):
    """Delete record"""

    data, code, valid = validator.delete(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code = resource.delete(request, properties_id)
            except:
                return {'code': 'properties/delete/fail'}, 404
        else:
            data, code = resource.delete(request, properties_id)

    return data, code
