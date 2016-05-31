# -*- coding: utf-8 -*-s
from __future__ import print_function
from django.views.decorators.csrf import ensure_csrf_cookie
from ..home.helpers import render_index
from django.utils.translation import ugettext


@ensure_csrf_cookie
def login(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Login on site')],
        'site_description': ugettext('Authorization on site'),
        'site_url': '/account/login'
    })


@ensure_csrf_cookie
def profile(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Profile')],
        'site_description': ugettext('Profile of user'),
        'site_url': '/account/profile'
    }, noindex=True)


@ensure_csrf_cookie
def reg(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Registration form')],
        'site_description': ugettext('Registration on site'),
        'site_url': '/account/reg'
    })


@ensure_csrf_cookie
def recovery(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Recovery access')],
        'site_description': ugettext('Recovery access to site'),
        'site_url': '/account/recovery'
    }, noindex=True)


@ensure_csrf_cookie
def reset(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Reset password')],
        'site_description': ugettext('Reset password for account'),
        'site_url': '/account/reset'
    }, noindex=True)


@ensure_csrf_cookie
def user_app(request):
    """Index page"""
    return render_index(request, {
        'site_title': [ugettext('Application')],
        'site_description': ugettext('Applications of user'),
        'site_url': '/account/user_app'
    }, noindex=True)
