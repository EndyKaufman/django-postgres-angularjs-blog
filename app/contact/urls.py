from django.conf.urls import url
import actions

urlpatterns = [
    url(r'^send', actions.send)
]