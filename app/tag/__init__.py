from django.conf.urls import patterns, url
from django.conf import settings

if settings.USE_MOCK:
    import app.tag.actions_mock as actions
else:
    import app.tag.actions

urlpatterns = [
    url(r'^create', actions.actionCreate),
    url(r'^update/(?P<id>[-\w]+)', actions.actionUpdate),
    url(r'^delete/(?P<id>[-\w]+)', actions.actionDelete),
    url(r'^item/(?P<id>[-\w]+)', actions.getItem),
    url(r'^list', actions.getList)
]
