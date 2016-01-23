from django.conf.urls import patterns, url
from django.conf import settings
import app.tag.actions
import app.tag.actions_fixture

if settings.USE_FIXTURE:
    urlpatterns = [
        # url(r'^create', actions.create),
        # url(r'^update/(?P<project_id>[-\w]+)', actions.update),
        # url(r'^delete/(?P<project_id>[-\w]+)', actions.delete),
        url(r'^list', actions_fixture.getList)
    ]
else:
    urlpatterns = [
        # url(r'^create', actions.create),
        # url(r'^update/(?P<project_id>[-\w]+)', actions.update),
        # url(r'^delete/(?P<project_id>[-\w]+)', actions.delete),
        url(r'^list', actions_fixture.getList)
    ]
