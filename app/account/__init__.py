from django.conf.urls import patterns, url
from django.conf import settings
import actions
import actions_mock

if settings.USE_MOCK:
        urlpatterns = [
                url(r'^login', actions_mock.actionLogin),
                url(r'^logout', actions_mock.actionLogout),
                url(r'^update', actions_mock.actionUpdate),
                url(r'^reg', actions_mock.actionReg),
                url(r'^delete', actions_mock.actionDelete),
                url(r'^recovery', actions_mock.actionRecovery),
                url(r'^resetpassword', actions_mock.actionResetpassword)
        ]
else:
        urlpatterns = [
                url(r'^login', actions.actionLogin),
                url(r'^logout', actions.actionLogout),
                url(r'^update', actions.actionUpdate),
                url(r'^reg', actions.actionReg),
                url(r'^delete', actions.actionDelete),
                url(r'^recovery', actions.actionRecovery),
                url(r'^resetpassword', actions.actionResetpassword)
        ]
