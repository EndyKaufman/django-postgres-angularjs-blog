from django.conf.urls import url
import app.tag.actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<tag_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<tag_id>[-\w]+)', actions.delete),
    url(r'^item/(?P<tag_id>[-\w]+)', actions.get_item),
    url(r'^search/(?P<search_text>[-\w]+)', actions.get_search),
    url(r'^list', actions.get_list)
]
