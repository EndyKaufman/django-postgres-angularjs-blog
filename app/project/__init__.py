from django.conf.urls import patterns, url
from django.conf import settings
import app.project.actions
import app.project.actions_mock

if settings.USE_MOCK:
    urlpatterns = [
        url(r'^create', actions_mock.actionCreate),
        url(r'^update/(?P<project_id>[-\w]+)', actions_mock.actionUpdate),
        url(r'^delete/(?P<project_id>[-\w]+)', actions_mock.actionDelete),
        url(r'^item/(?P<project_name>[-\w]+)', actions_mock.getItem),
        url(r'^search/(?P<search_text>[-\w]+)', actions_mock.getSearch),
        url(r'^listbytag/(?P<tag_text>[-\w]+)', actions_mock.getListByTag),
        url(r'^list', actions_mock.getList)
    ]
else:
    urlpatterns = [
        url(r'^create', actions.actionCreate),
        url(r'^update/(?P<project_id>[-\w]+)', actions.actionUpdate),
        url(r'^delete/(?P<project_id>[-\w]+)', actions.actionDelete),
        url(r'^item/(?P<project_name>[-\w]+)', actions.getItem),
        url(r'^search/(?P<search_text>[-\w]+)', actions.getSearch),
        url(r'^listbytag/(?P<tag_text>[-\w]+)', actions.getListByTag),
        url(r'^list', actions.getList)
    ]
