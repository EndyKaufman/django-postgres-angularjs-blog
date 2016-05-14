from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<file_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<file_id>[-\w]+)', actions.delete),
    url(r'^item/(?P<file_id>[-\w]+)', actions.get_item),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^list', actions.get_list)
]
