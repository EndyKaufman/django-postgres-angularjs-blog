# -*- coding: utf-8 -*-s
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie
from ..home.helpers import render_index
from project import settings, helpers
import resource
from django.utils.translation import ugettext


@ensure_csrf_cookie
def get_list(request):
    """List data"""
    strings = {
        'site_title': [ugettext('Posts')],
        'site_description': ugettext('Posts descriptions'),
        'site_url': 'post'
    }
    return render_index(request, strings)


@ensure_csrf_cookie
def get_item_by_name(request, post_name):
    """Item data"""

    if settings.ENV == 'production':
        try:
            item = resource.get_object_by_name(request, post_name)
        except:
            item = False
    else:
        item = resource.get_object_by_name(request, post_name)
    if item:
        strings = {
            'site_title': [item.title, ugettext('Posts')],
            'site_description': item.description,
            'site_url': 'project/%s' % item.name
        }
        images = list(item.images.all())
        if images:
            strings['site_image'] = helpers.get_thumbnail_url(request, images[0].src)
        return render_index(request, strings)
    else:
        raise Http404


@ensure_csrf_cookie
def update(request, post_name):
    """Item data"""

    if settings.ENV == 'production':
        try:
            item = resource.get_object_by_name(request, post_name)
        except:
            item = False
    else:
        item = resource.get_object_by_name(request, post_name)
    if item:
        strings = {
            'site_title': [item.title, ugettext('Posts')],
            'site_description': item.description,
            'site_url': 'project/update/%s' % item.name
        }
        images = list(item.images.all())
        if images:
            strings['site_image'] = helpers.get_thumbnail_url(request, images[0].src)
        return render_index(request, strings, noindex=True)
    else:
        raise Http404
