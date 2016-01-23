from django.conf.urls import patterns, url
from django.conf import settings
import actions
import actions_fixture

if settings.USE_FIXTURE:
        urlpatterns = [
                url(r'^login', actions_fixture.postLogin),
                url(r'^logout', actions_fixture.postLogout)
        ]
else:
        urlpatterns = [
                url(r'^login', actions_fixture.postLogin),
                url(r'^logout', actions_fixture.postLogout)
        ]
