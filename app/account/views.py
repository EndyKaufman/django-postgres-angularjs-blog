# -*- coding: utf-8 -*-s
from django.views.decorators.csrf import ensure_csrf_cookie
from app.home.helpers import render_index


@ensure_csrf_cookie
def login(request):
    """Index page"""
    return render_index(request, {
        'site_title': ['Login on site'],
        'site_description': 'Authorization on site',
        'site_url': '/account/login'
    })


@ensure_csrf_cookie
def profile(request):
    """Index page"""
    return render_index(request, {
        'site_title': ['Profile'],
        'site_description': 'Profile of user',
        'site_url': '/account/profile'
    })


@ensure_csrf_cookie
def reg(request):
    """Index page"""
    return render_index(request, {
        'site_title': ['Registration form'],
        'site_description': 'Registration on site',
        'site_url': '/account/reg'
    })


@ensure_csrf_cookie
def recovery(request):
    """Index page"""
    return render_index(request, {
        'site_title': ['Recovery access'],
        'site_description': 'Recovery access to site',
        'site_url': '/account/recovery'
    })


@ensure_csrf_cookie
def reset(request):
    """Index page"""
    return render_index(request, {
        'site_title': ['Reset password'],
        'site_description': 'Reset password for account',
        'site_url': '/account/reset'
    })


@ensure_csrf_cookie
def user_app(request):
    """Index page"""
    return render_index(request, {
        'site_title': ['User app'],
        'site_description': 'User app of user',
        'site_url': '/account/user_app'
    })
