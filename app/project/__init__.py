from django.conf.urls import patterns, url
import app.project.actions

urlpatterns = [
    # url(r'^create', actions.create),
    # url(r'^update/(?P<project_id>[-\w]+)', actions.update),
    # url(r'^delete/(?P<project_id>[-\w]+)', actions.delete),
    url(r'^item/(?P<project_name>[-\w]+)', actions.getItem),
    url(r'^search/(?P<search_text>[-\w]+)', actions.getSearch),
    url(r'^listbytag/(?P<tag_text>[-\w]+)', actions.getListByTag),
    url(r'^list', actions.getList)
]
