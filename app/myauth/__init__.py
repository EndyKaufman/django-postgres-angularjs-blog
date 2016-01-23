from django.conf.urls import patterns, url
import actions

urlpatterns = [
        url(r'^login', actions.postLogin),
        url(r'^logout', actions.postLogout)
]
