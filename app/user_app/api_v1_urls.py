from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^create', actions.create),
    url(r'^update/(?P<user_app_id>[-\w]+)', actions.update),
    url(r'^delete/(?P<user_app_id>[-\w]+)', actions.delete),
    url(r'^(?P<user_app_client_id>[-\w]+)', actions.get_item_by_client_id),
    url(r'^$', actions.get_list)
]
