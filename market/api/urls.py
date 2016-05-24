from django.conf.urls import url
from .routes import venues, organizers

urlpatterns = [
    url(r'^venues/', venues),
    url(r'^organizers/', organizers),
]