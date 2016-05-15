from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^login', actions.login),
    url(r'^logout', actions.logout),
    url(r'^update', actions.update),
    url(r'^reg', actions.reg),
    url(r'^delete', actions.delete),
    url(r'^recovery', actions.recovery),
    url(r'^reset', actions.reset)
]
