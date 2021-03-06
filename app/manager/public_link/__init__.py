from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<public_link_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<public_link_id>[-\w]+)', actions.delete),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^(?P<public_link_src>[-\w]+)', actions.get_item_by_name),
    url(r'^$', actions.get_list)
]
