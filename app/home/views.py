# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
import json
from app.manager.meta_tag import resource as meta_tag_resource
from app.manager.properties import resource as properties_resource


# Create your views here.
@ensure_csrf_cookie
def index(request):
    """Home page maker"""
    from helpers import getConfig

    config = getConfig(request)
    config['properties'] = properties_resource.get_list_of_names(request,
                                                                 ['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME',
                                                                  'SITE_LOGO'])

    meta_tag_list = meta_tag_resource.get_list(request)

    properties_list = properties_resource.get_list_of_names(request,
                                                            ['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME', 'SITE_LOGO',
                                                             'HOME_HEADER_BOTTOM_HTML',
                                                             'HOME_BODY_TOP_HTML', 'HOME_BODY_BOTTOM_HTML'])

    try:
        HTTP_USER_AGENT = request.META['HTTP_USER_AGENT']
    except:
        HTTP_USER_AGENT = 'EMPTY'

    if "_escaped_fragment_" not in request.GET and 'Prerender' not in HTTP_USER_AGENT:
        escaped_fragment_tag = '<meta name="fragment" content="!">'
    else:
        escaped_fragment_tag = ''

    return render(request, 'home/templates/%s/index.htm' % settings.THEME, {
        'host_url': '//' + request.get_host(),
        'config': json.dumps(config, sort_keys=True, indent=4),
        'settings': settings,
        'meta_tag_list': meta_tag_list,
        'properties_list': properties_list,
        'escaped_fragment_tag': escaped_fragment_tag
    })


def robots_txt(request):
    """Robots.txt page"""
    properties_list = properties_resource.get_list_of_names(request, ['ROBOT_TXT'])
    return render(request, 'home/templates/%s/robots.txt' % settings.THEME, {'properties_list': properties_list})


def sitemap_xml(request):
    """Sitemap page"""
    from helpers import getConfig
    config = getConfig(request)

    from app.project.models import Project
    project_list = Project.objects.all().order_by('-created').all()

    from app.post.models import Post
    post_list = Post.objects.all().order_by('-created').all()

    return render(request, 'home/templates/%s/sitemap.xml' % settings.THEME, {
        'config': config,
        'project_list': project_list,
        'post_list': post_list
    })
