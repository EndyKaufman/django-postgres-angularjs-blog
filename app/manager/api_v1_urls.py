from django.conf.urls import include, url
import meta_tag, public_link, properties, html_cache

urlpatterns = [
    url(r'^meta_tag/', include(meta_tag)),
    url(r'^public_link/', include(public_link)),
    url(r'^properties/', include(properties)),
    url(r'^html_cache/', include(html_cache))
]
