from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<tag_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<tag_id>[-\w]+)', actions.delete),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^(?P<tag_id>[-\w]+)', actions.get_item),
    url(r'^$', actions.get_list)
]
