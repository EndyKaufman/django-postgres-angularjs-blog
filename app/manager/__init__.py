from django.conf.urls import include, url
import meta_tag, public_link

urlpatterns = [
    url(r'^meta_tag/', include(meta_tag)),
    url(r'^public_link/', include(public_link))
]
