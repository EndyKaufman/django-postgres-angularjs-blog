from django.conf.urls import url
import app.contact.actions

urlpatterns = [
    url(r'^send', actions.send)
]