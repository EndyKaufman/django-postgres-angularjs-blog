from django.conf.urls import url
from oauth2_provider import views


urlpatterns = [
    url(r'^token/$', views.TokenView.as_view(), name="token"),
    url(r'^revoke_token/$', views.RevokeTokenView.as_view(), name="revoke-token"),
]
