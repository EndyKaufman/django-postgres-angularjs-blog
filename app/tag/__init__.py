from django.conf.urls import patterns, url
from django.conf import settings

if settings.USE_MOCK:
    import app.tag.actions_mock as actions
else:
    import app.tag.actions
urlpatterns = [
    # url(r'^create', actions.create),
    # url(r'^update/(?P<project_id>[-\w]+)', actions.update),
    # url(r'^delete/(?P<project_id>[-\w]+)', actions.delete),
    url(r'^list', actions.getList)
]
