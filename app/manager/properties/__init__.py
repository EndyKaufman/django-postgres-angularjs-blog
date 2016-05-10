from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<properties_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<properties_id>[-\w]+)', actions.delete),
    url(r'^item/(?P<properties_name>[-\w]+)', actions.get_item_by_name),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^list', actions.get_list)
]
