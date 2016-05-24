from django.conf.urls import url
from django.http import HttpResponse
from .views import main, venues

# import pdb; pdb.set_trace()
urlpatterns = [
    url(r'^venues/', venues),
    url(r'^', main),
]

