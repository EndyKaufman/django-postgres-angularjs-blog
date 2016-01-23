from django.conf.urls import patterns, url
from django.conf import settings
import app.project.actions
import app.project.actions_fixture

if settings.USE_FIXTURE:
    urlpatterns = [
        url(r'^create', actions_fixture.actionCreate),
        url(r'^update/(?P<project_id>[-\w]+)', actions_fixture.actionUpdate),
        url(r'^delete/(?P<project_id>[-\w]+)', actions_fixture.actionDelete),
        url(r'^item/(?P<project_name>[-\w]+)', actions_fixture.getItem),
        url(r'^search/(?P<search_text>[-\w]+)', actions_fixture.getSearch),
        url(r'^listbytag/(?P<tag_text>[-\w]+)', actions_fixture.getListByTag),
        url(r'^list', actions_fixture.getList)
    ]
else:
    urlpatterns = [
        url(r'^create', actions_fixture.actionCreate),
        url(r'^update/(?P<project_id>[-\w]+)', actions_fixture.actionUpdate),
        url(r'^delete/(?P<project_id>[-\w]+)', actions_fixture.actionDelete),
        url(r'^item/(?P<project_name>[-\w]+)', actions_fixture.getItem),
        url(r'^search/(?P<search_text>[-\w]+)', actions_fixture.getSearch),
        url(r'^listbytag/(?P<tag_text>[-\w]+)', actions_fixture.getListByTag),
        url(r'^list', actions_fixture.getList)
    ]
