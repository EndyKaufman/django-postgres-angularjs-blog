from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<post_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<post_id>[-\w]+)', actions.delete),
    url(r'^item/(?P<post_name>[-\w]+)', actions.get_item_by_name),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^listbytag/(?P<tag_text>[-\w]+)', actions.get_list_by_tag),
    url(r'^list', actions.get_list)
]
