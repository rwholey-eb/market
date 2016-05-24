from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from db.models import Venues, Organizers

@login_required(login_url='/auth/login')
def main(request):
    context = {
        'venues': Venues.objects.all(),
        'csrf_token': csrf,
        'isAuth': request.user.is_authenticated(),
    }
    return render_to_response('index.html', RequestContext(request,context))

@login_required(login_url='/auth/login')
def venues(request):
    return HttpResponse('venues')
