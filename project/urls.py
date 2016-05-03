"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import sys
import app.file
import app.account
import app.tag
import app.project
import app.contact
import app.post
import app.manager
import app.home.views
import app.home

admin.autodiscover()

urlpatterns = [
                  url(r'^robots\.txt$', app.home.views.robots_txt, name='robots_txt'),
                  url(r'^sitemap\.xml$', app.home.views.sitemap_xml, name='sitemap_xml'),
                  url(r'^$', app.home.views.index, name='index'),
                  url(r'^api/v1/file/', include(app.file)),
                  url(r'^api/v1/account/', include(app.account)),
                  url(r'^api/v1/tag/', include(app.tag)),
                  url(r'^api/v1/project/', include(app.project)),
                  url(r'^api/v1/post/', include(app.post)),
                  url(r'^api/v1/contact/', include(app.contact)),
                  url(r'^api/v1/manager/', include(app.manager))
                  # url(r'^admin/', admin.site.urls)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
                  url(r'^.*$', app.home.views.index, name='index')
              ]
