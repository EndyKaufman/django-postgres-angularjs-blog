from django.conf.urls import url
import views

urlpatterns = [
    url(r'^create', views.get_list),
    url(r'^update/(?P<project_name>[-\w]+)', views.update),
    url(r'^(?P<project_name>[-\w]+)', views.get_item_by_name)
]
