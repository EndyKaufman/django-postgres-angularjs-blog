from django.conf.urls import url
from django.conf import settings
import app.file.actions
import app.file.actions_mock

if settings.USE_MOCK:
    urlpatterns = [
        url(r'^create', actions_mock.actionCreate),
        url(r'^update/(?P<file_id>[-\w]+)', actions_mock.actionUpdate),
        url(r'^delete/(?P<file_id>[-\w]+)', actions_mock.actionDelete),
        url(r'^item/(?P<file_id>[-\w]+)', actions_mock.getItem),
        url(r'^search/(?P<search_text>[-\w]+)', actions_mock.getSearch),
        url(r'^list', actions_mock.getList)
    ]
else:
    urlpatterns = [
        url(r'^create', actions.actionCreate),
        url(r'^update/(?P<file_id>[-\w]+)', actions.actionUpdate),
        url(r'^delete/(?P<file_id>[-\w]+)', actions.actionDelete),
        url(r'^item/(?P<file_id>[-\w]+)', actions.getItem),
        url(r'^search/(?P<search_text>[-\w]+)', actions.getSearch),
        url(r'^list', actions.getList)
    ]
