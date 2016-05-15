from django.conf.urls import url
import views

urlpatterns = [
    url(r'^/login', views.login),
    url(r'^/profile', views.profile),
    url(r'^/reg', views.reg),
    url(r'^/recovery', views.recovery),
    url(r'^/reset', views.reset),
    url(r'^/user_app', views.user_app)
]
