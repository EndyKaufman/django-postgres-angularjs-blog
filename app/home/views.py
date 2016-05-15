# -*- coding: utf-8 -*-s
from django.views.decorators.csrf import ensure_csrf_cookie
import helpers


# Create your views here.
@ensure_csrf_cookie
def index(request):
    """Index page"""
    return helpers.render_index(request, {})


def robots_txt(request):
    """Robots.txt page"""
    return helpers.render_robots_txt(request)


def sitemap_xml(request):
    """Sitemap page"""
    return helpers.render_sitemap_xml(request)
