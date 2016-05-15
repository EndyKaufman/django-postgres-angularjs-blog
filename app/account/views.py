# -*- coding: utf-8 -*-s
from django.views.decorators.csrf import ensure_csrf_cookie
from app.home.helpers import render_index


@ensure_csrf_cookie
def login(request):
    """Index page"""
    return render_index(request, {
        'site_title': [u'Login on site'],
        'site_description': [u'Authorization on site'],
        'site_url': '/account/login'
    })


@ensure_csrf_cookie
def profile(request):
    """Index page"""
    return render_index(request, {
        'site_title': [u'Profile'],
        'site_description': [u'Profile of user'],
        'site_url': '/account/profile'
    })


@ensure_csrf_cookie
def reg(request):
    """Index page"""
    return render_index(request, {
        'site_title': [u'Registration form'],
        'site_description': [u'Registration on site'],
        'site_url': '/account/reg'
    })


@ensure_csrf_cookie
def recovery(request):
    """Index page"""
    return render_index(request, {
        'site_title': [u'Recovery access'],
        'site_description': [u'Recovery access to site'],
        'site_url': '/account/recovery'
    })


@ensure_csrf_cookie
def reset(request):
    """Index page"""
    return render_index(request, {
        'site_title': [u'Reset password'],
        'site_description': [u'Reset password for account'],
        'site_url': '/account/reset'
    })
