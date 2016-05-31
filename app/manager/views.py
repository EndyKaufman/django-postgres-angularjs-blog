# -*- coding: utf-8 -*-s
from __future__ import print_function
from django.views.decorators.csrf import ensure_csrf_cookie
from ..home.helpers import render_index
from django.utils.translation import ugettext


@ensure_csrf_cookie
def meta_tag(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Meta tags'), ugettext('Manager')],
        'site_description': ugettext('Meta tags description'),
        'site_url': '/manager/meta_tag'
    }, noindex=True)


@ensure_csrf_cookie
def public_link(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Public links'), ugettext('Manager')],
        'site_description': ugettext('Public links description'),
        'site_url': '/manager/public_link'
    }, noindex=True)


@ensure_csrf_cookie
def properties(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Properties'), ugettext('Manager')],
        'site_description': ugettext('Properties description'),
        'site_url': '/manager/properties'
    }, noindex=True)


@ensure_csrf_cookie
def html_cache(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Html cache'), ugettext('Manager')],
        'site_description': ugettext('Html cache description'),
        'site_url': '/manager/html_cache'
    }, noindex=True)
