# -*- coding: utf-8 -*-s
from django.views.decorators.csrf import ensure_csrf_cookie
from app.home.helpers import render_index


@ensure_csrf_cookie
def contact(request):
    """Index page"""
    return render_index(request, {
        'site_title': [u'Contact us'],
        'site_description': [u'Contact us'],
        'site_url': '/contact'
    })