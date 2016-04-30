from django.conf.urls import url
import app.post.actions

urlpatterns = [
    url(r'^create', actions.actionCreate),
    url(r'^update/(?P<post_id>[-\w]+)', actions.actionUpdate),
    url(r'^delete/(?P<post_id>[-\w]+)', actions.actionDelete),
    url(r'^item/(?P<post_name>[-\w]+)', actions.getItem),
    url(r'^search/(?P<search_text>[-\w]+)', actions.getSearch),
    url(r'^listbytag/(?P<tag_text>[-\w]+)', actions.getListByTag),
    url(r'^list', actions.getList)
]
