from django.conf.urls import url
import views

urlpatterns = [
    url(r'^meta_tag', views.meta_tag),
    url(r'^public_link', views.public_link),
    url(r'^properties', views.properties),
    url(r'^html_cache', views.html_cache)
]
