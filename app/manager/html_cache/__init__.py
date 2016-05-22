from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<html_cache_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<html_cache_id>[-\w]+)', actions.delete),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^(?P<html_cache_url>[-\w]+)', actions.get_item_by_url),
    url(r'^$', actions.get_list)
]
