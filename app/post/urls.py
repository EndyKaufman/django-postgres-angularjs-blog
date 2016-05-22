from django.conf.urls import url
import views

urlpatterns = [
    url(r'^create', views.get_list),
    url(r'^update/(?P<post_name>[-\w]+)', views.get_item_by_name),
    url(r'^(?P<post_name>[-\w]+)', views.get_item_by_name),
    url(r'^$', views.get_list)
]
