from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.actionCreate),
    url(r'^update/(?P<id>[-\w]+)', actions.actionUpdate),
    url(r'^delete/(?P<id>[-\w]+)', actions.actionDelete),
    url(r'^item/(?P<id>[-\w]+)', actions.getItem),
    url(r'^list', actions.getList)
]
