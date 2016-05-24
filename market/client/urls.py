from django.conf.urls import url
from django.http import HttpResponse
from .views import main

urlpatterns = [
    url(r'^', main),
]

