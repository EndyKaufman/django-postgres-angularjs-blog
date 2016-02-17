from django.conf.urls import patterns, url
from django.conf import settings
import actions
import actions_fixture

if settings.USE_FIXTURE:
        urlpatterns = [
                url(r'^login', actions_fixture.actionLogin),
                url(r'^logout', actions_fixture.actionLogout),
                url(r'^update', actions_fixture.actionUpdate),
                url(r'^reg', actions_fixture.actionReg),
                url(r'^delete', actions_fixture.actionDelete)
        ]
else:
        urlpatterns = [
                url(r'^login', actions.actionLogin),
                url(r'^logout', actions.actionLogout),
                url(r'^update', actions.actionUpdate),
                url(r'^reg', actions.actionReg),
                url(r'^delete', actions.actionDelete)
        ]
