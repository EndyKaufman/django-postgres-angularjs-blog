# -*- coding: utf-8 -*-s
from django.views.decorators.csrf import ensure_csrf_cookie
from ..home.helpers import render_index
from django.utils.translation import ugettext


@ensure_csrf_cookie
def index(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Contact us')],
        'site_description': ugettext('Contact us description'),
        'site_url': '/contact'
    })