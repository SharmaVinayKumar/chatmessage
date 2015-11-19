"""chatmessage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from chat.views import LoginView, ChatView, LogOutView, SignUpView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^signup/$', SignUpView.as_view(), name="signup"),
    url(r'^logout/$', LogOutView.as_view(), name ="logout" ),
    url(r'^home/(?P<user_id>\d+)/$', ChatView.as_view(), name="user_list"),
    url(r'^home/$', ChatView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
]