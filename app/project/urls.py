from django.conf.urls import url
import views

urlpatterns = [
    url(r'^/(?P<project_name>[-\w]+)', views.get_item_by_name),
    url(r'^$', views.get_list)
]
