from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from django.http import HttpResponse
from .auth import app_login, app_signup, app_logout

import client, api
from client import urls
from api import urls

def redirect_home(r):
    return redirect('/client/')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/login', app_login),
    url(r'^auth/signup', app_signup),
    url(r'^auth/logout', app_logout),
    url(r'^client/', include(client.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^/', redirect_home),
    url(r'^', redirect_home),
]
