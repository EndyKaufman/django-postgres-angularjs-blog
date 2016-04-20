from django.conf.urls import url
from django.conf import settings

if settings.USE_MOCK:
    import app.file.actions_mock as actions
else:
    import app.file.actions

urlpatterns = [
    url(r'^create', actions.actionCreate),
    url(r'^update/(?P<file_id>[-\w]+)', actions.actionUpdate),
    url(r'^delete/(?P<file_id>[-\w]+)', actions.actionDelete),
    url(r'^item/(?P<file_id>[-\w]+)', actions.getItem),
    url(r'^search/(?P<search_text>[-\w]+)', actions.getSearch),
    url(r'^list', actions.getList)
]
