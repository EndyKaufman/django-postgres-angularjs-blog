from django.conf.urls import url
from django.conf import settings

if settings.USE_MOCK:
    import app.project.actions_mock as actions
else:
    import app.project.actions

urlpatterns = [
    url(r'^create', actions.actionCreate),
    url(r'^update/(?P<project_id>[-\w]+)', actions.actionUpdate),
    url(r'^delete/(?P<project_id>[-\w]+)', actions.actionDelete),
    url(r'^item/(?P<project_name>[-\w]+)', actions.getItem),
    url(r'^search/(?P<search_text>[-\w]+)', actions.getSearch),
    url(r'^listbytag/(?P<tag_text>[-\w]+)', actions.getListByTag),
    url(r'^list', actions.getList)
]
