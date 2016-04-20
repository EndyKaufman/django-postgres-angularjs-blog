from django.conf.urls import patterns, url
from django.conf import settings

if settings.USE_MOCK:
    import app.post.actions_mock as actions
else:
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
