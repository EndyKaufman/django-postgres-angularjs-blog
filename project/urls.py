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
import app.home.views
import app.home

admin.autodiscover()

urlpatterns = [
                  url(r'^$', app.home.views.index, name='index'),
                  url(r'^file/', include(app.file)),
                  url(r'^account/', include(app.account)),
                  url(r'^tag/', include(app.tag)),
                  url(r'^project/', include(app.project)),
                  url(r'^post/', include(app.post)),
                  url(r'^admin/', admin.site.urls)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
                  url(r'^.*$', app.home.views.index, name='index')
              ]

if 'livereload' in sys.argv:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
