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
import app.file.api_v1_urls
import app.account.urls
import app.account.api_v1_urls
import app.account.oauth2_urls
import app.tag.api_v1_urls
import app.contact.views
import app.contact.urls
import app.contact.api_v1_urls
import app.post.views
import app.post.urls
import app.post.api_v1_urls
import app.project.views
import app.project.urls
import app.project.api_v1_urls
import app.manager.api_v1_urls
import app.user_app.api_v1_urls
import app.home.views
import app.home

admin.autodiscover()

urlpatterns = []
urlpatterns = urlpatterns + [
    url(r'^robots\.txt$', app.home.views.robots_txt, name='robots_txt'),
    url(r'^sitemap\.xml$', app.home.views.sitemap_xml, name='sitemap_xml'),
    url(r'^$', app.home.views.index, name='index')]

urlpatterns = urlpatterns + [
    url(r'^api/v1/file/', include(app.file.api_v1_urls)),
    url(r'^api/v1/account/', include(app.account.api_v1_urls)),
    url(r'^api/v1/contact/', include(app.contact.api_v1_urls)),
    url(r'^api/v1/post/', include(app.post.api_v1_urls)),
    url(r'^api/v1/project/', include(app.project.api_v1_urls)),
    url(r'^api/v1/tag/', include(app.tag.api_v1_urls)),
    url(r'^api/v1/manager/', include(app.manager.api_v1_urls)),
    url(r'^api/v1/user_app/', include(app.user_app.api_v1_urls))]

urlpatterns = urlpatterns + [
    url(r'^contact', app.contact.views.index, name='index'),
    url(r'^post', app.post.views.get_list, name='get_list'),
    url(r'^project', app.project.views.get_list, name='get_list'),

    url(r'^oauth2/', include(app.account.oauth2_urls, namespace='oauth2_provider')),
    url(r'^account/', include(app.account.urls)),
    url(r'^contact/', include(app.contact.urls)),
    url(r'^post/', include(app.post.urls)),
    url(r'^project/', include(app.project.urls)),

    url(r'^tag/.*$', app.home.views.index, name='index'),
    url(r'^search/.*$', app.home.views.index, name='index'),
    url(r'^manager/.*$', app.home.views.index, name='index'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^.*$', app.home.views.index, name='index')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
