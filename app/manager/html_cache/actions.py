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
            return {'code': 'html_cache/get_list/fail'}, 404
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
            return {'code': 'html_cache/get_search/fail'}, 404
    else:
        data, code, items = resource.get_search(request, search_text)

    return data, code


@json_view
def get_item_by_url(request, html_cache_url):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item_by_url(request, html_cache_url)
        except:
            return {'code': 'html_cache/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item_by_url(request, html_cache_url)
    return data, code


@json_view
def get_item(request, html_cache_id):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item(request, html_cache_id)
        except:
            return {'code': 'html_cache/get_item/fail'}, 404
    else:
        data, code, item = resource.get_item(request, html_cache_id)
    return data, code


@json_view
def update(request, html_cache_id):
    """Update record"""

    data, code, valid = validator.update(request, html_cache_id)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code, item = resource.update(request, html_cache_id)
            except:
                return {'code': 'html_cache/update/fail'}, 404
        else:
            data, code, item = resource.update(request, html_cache_id)

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
                return {'code': 'html_cache/create/fail'}, 404
        else:
            data, code, item = resource.create(request)

    return data, code


@json_view
def delete(request, html_cache_id):
    """Delete record"""

    data, code, valid = validator.delete(request)

    if valid:
        if settings.ENV == 'production':
            try:
                data, code = resource.delete(request, html_cache_id)
            except:
                return {'code': 'html_cache/delete/fail'}, 404
        else:
            data, code = resource.delete(request, html_cache_id)

    return data, code
