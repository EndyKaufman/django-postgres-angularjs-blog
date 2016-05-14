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
import app.file.urls
import app.account.urls
import app.account.oauth_urls
import app.tag.urls
import app.project.urls
import app.contact.urls
import app.post.urls
import app.manager.urls
import app.user_app.urls
import app.home.views
import app.home

admin.autodiscover()

urlpatterns = []
urlpatterns = urlpatterns + [
    url(r'^robots\.txt$', app.home.views.robots_txt, name='robots_txt'),
    url(r'^sitemap\.xml$', app.home.views.sitemap_xml, name='sitemap_xml'),
    url(r'^$', app.home.views.index, name='index')]

app_list = ['file', 'account', 'tag', 'project', 'post', 'contact', 'manager', 'user_app']

urlpatterns = urlpatterns + [
    url(r'^api/v1/file/', include(app.file.urls)),
    url(r'^api/v1/account/', include(app.account.urls)),
    url(r'^api/v1/tag/', include(app.tag.urls)),
    url(r'^api/v1/project/', include(app.project.urls)),
    url(r'^api/v1/post/', include(app.post.urls)),
    url(r'^api/v1/contact/', include(app.contact.urls)),
    url(r'^api/v1/manager/', include(app.manager.urls)),
    url(r'^api/v1/user_app/', include(app.user_app.urls))]

urlpatterns = urlpatterns + [
    url(r'^oauth2/', include('app.account.oauth_urls', namespace='oauth2_provider')),
    # url(r'^admin/', admin.site.urls)
    url(r'^file/.*$', app.home.views.index, name='index'),
    url(r'^account/.*$', app.home.views.index, name='index'),
    url(r'^profile/.*$', app.home.views.index, name='index'),
    url(r'^login/.*$', app.home.views.index, name='index'),
    url(r'^tag/.*$', app.home.views.index, name='index'),
    url(r'^project/.*$', app.home.views.index, name='index'),
    url(r'^post/.*$', app.home.views.index, name='index'),
    url(r'^contact/.*$', app.home.views.index, name='index'),
    url(r'^manager/.*$', app.home.views.index, name='index'),
    url(r'^user_app/.*$', app.home.views.index, name='index'),
    # url(r'^.*$', app.home.views.index, name='index')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
