# -*- coding: utf-8 -*-s
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie
from app.home.helpers import render_index
from project import settings
import resource
from django.utils.translation import ugettext


@ensure_csrf_cookie
def get_list(request):
    """List data"""
    strings = {
        'site_title': [ugettext('Projects')],
        'site_description': ugettext('List their own more and more projects'),
        'site_url': 'project'
    }
    return render_index(request, strings)


@ensure_csrf_cookie
def get_item_by_name(request, project_name):
    """Item data"""

    if settings.ENV == 'production':
        try:
            data, code, item = resource.get_item_by_name(request, project_name)
        except:
            item = False
    else:
        data, code, item = resource.get_item_by_name(request, project_name)
    if item:
        item_data = data['data'][0]
        strings = {
            'site_title': [item_data['title'], ugettext('Projects')],
            'site_description': item_data['description'],
            'site_url': 'project/%s' % item_data['name']
        }
        if len(item_data['images']) > 0:
            strings['site_image'] = item_data['images'][0]['src_thumbnail_url']
        return render_index(request, strings)
    else:
        raise Http404
