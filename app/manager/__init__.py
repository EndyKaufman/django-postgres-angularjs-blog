from django.conf.urls import include, url
import meta_tag

urlpatterns = [
    url(r'^meta_tag/', include(meta_tag))
]
