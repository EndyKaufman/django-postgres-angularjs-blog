from django.conf.urls import url
from django.conf import settings

if settings.USE_MOCK:
    import actions_mock as actions
else:
    import actions

urlpatterns = [
    url(r'^login', actions.actionLogin),
    url(r'^logout', actions.actionLogout),
    url(r'^update', actions.actionUpdate),
    url(r'^reg', actions.actionReg),
    url(r'^delete', actions.actionDelete),
    url(r'^recovery', actions.actionRecovery),
    url(r'^resetpassword', actions.actionResetpassword)
]
