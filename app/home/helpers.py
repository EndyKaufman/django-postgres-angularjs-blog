# -*- coding: utf-8 -*-

from project import helpers
from django.shortcuts import render
from django.conf import settings
import json
from ..manager.meta_tag import resource as meta_tag_resource
from ..manager.properties import resource as properties_resource
from django.utils.translation import get_language


def get_config(request):
    protocol = 'https' if request.is_secure() else 'http'

    config = {}

    config['host'] = '%s://%s' % (protocol, request.get_host())
    config['host_name'] = '%s://%s' % (protocol, request.get_host().decode('idna'))
    config['current_lang'] = get_language()
    config['lang'] = settings.LANGUAGE_CODE

    lang_list = []
    for (lang, title) in settings.LANGUAGES:
        lang_list.append({'code': lang, 'title': title})

    config['lang_list'] = lang_list

    user = helpers.get_user(request)

    if not user or user is None:
        config['user'] = {}
    else:
        config['user'] = user.get_user_data().copy()

    return config


def render_index(request, strings, template='home/templates/%s/index.htm', noindex=False):
    config = get_config(request)
    config['properties'] = properties_resource.get_list_of_names(['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME',
                                                                  'SITE_LOGO'])

    strings = helpers.set_null_values_if_not_exist(strings, ['site_title', 'site_description', 'site_name',
                                                             'site_image', 'site_type', 'site_url'])
    if strings['site_title'] is None:
        strings['site_title'] = config['properties']['SITE_TITLE']
        strings['short_site_title'] = config['properties']['SITE_TITLE']
    else:
        strings['site_title'].append(config['properties']['SITE_TITLE'])
        strings['short_site_title'] = strings['site_title'][0]
        strings['site_title'] = strings['site_title'][0]

    if strings['site_description'] is None:
        strings['site_description'] = config['properties']['SITE_DESCRIPTION']

    if strings['site_name'] is None:
        strings['site_name'] = config['properties']['SITE_NAME']

    if strings['site_image'] is None:
        strings['site_image'] = config['properties']['SITE_LOGO']

    if strings['site_type'] is None:
        strings['site_type'] = 'website'

    if strings['site_url'] is None:
        strings['site_url'] = config['host_name']
        strings['short_site_url'] = ''
    else:
        temp_list = []
        temp_list.append(config['host_name'])
        temp_list.append(strings['site_url'])
        strings['short_site_url'] = '/%s' % strings['site_url']
        strings['site_url'] = '/'.join(temp_list)

    meta_tag_list = meta_tag_resource.get_list_as_objects()

    properties_list = properties_resource.get_list_of_names(['SITE_TITLE', 'SITE_DESCRIPTION', 'SITE_NAME', 'SITE_LOGO',
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

    if noindex:
        noindex_tag = '<meta name="robots" content="noindex,nofollow" />'
    else:
        noindex_tag = ''

    return render(request, template % settings.THEME, {
        'host_name': config['host_name'],
        'host_url': '//' + request.get_host(),
        'config': json.dumps(config, sort_keys=True, indent=4),
        'current_lang': get_language(),
        'lang': settings.LANGUAGE_CODE,
        'lang_list': config['lang_list'],
        'settings': settings,
        'meta_tag_list': meta_tag_list,
        'properties_list': properties_list,
        'escaped_fragment_tag': escaped_fragment_tag,
        'noindex_tag': noindex_tag,
        'strings': strings
    })


def render_404(request, strings):
    return render_index(request, strings)


def render_robots_txt(request):
    properties_list = properties_resource.get_list_of_names(['ROBOT_TXT'])
    return render(request, 'home/templates/robots.txt', {'properties_list': properties_list})


def render_sitemap_xml(request):
    from helpers import get_config
    config = get_config(request)

    from ..project.models import Project
    project_list = Project.objects.all().order_by('-created').all()

    from ..post.models import Post
    post_list = Post.objects.all().order_by('-created').all()

    return render(request, 'home/templates/%s/sitemap.xml' % settings.THEME, {
        'config': config,
        'project_list': project_list,
        'post_list': post_list,
        'current_lang': get_language(),
        'lang': settings.LANGUAGE_CODE,
        'lang_list': config['lang_list'],
    })
