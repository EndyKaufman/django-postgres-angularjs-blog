from django.conf.urls import patterns, url
from django.conf import settings
import app.tag.actions
import app.tag.actions_mock

if settings.USE_MOCK:
    urlpatterns = [
        # url(r'^create', actions.create),
        # url(r'^update/(?P<project_id>[-\w]+)', actions.update),
        # url(r'^delete/(?P<project_id>[-\w]+)', actions.delete),
        url(r'^list', actions_mock.getList)
    ]
else:
    urlpatterns = [
        # url(r'^create', actions.create),
        # url(r'^update/(?P<project_id>[-\w]+)', actions.update),
        # url(r'^delete/(?P<project_id>[-\w]+)', actions.delete),
        url(r'^list', actions.getList)
    ]
