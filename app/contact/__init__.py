from django.conf.urls import patterns, url
from django.conf import settings
import app.contact.actions

urlpatterns = [
    url(r'^send', actions.actionSend)
]