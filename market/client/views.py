from django.shortcuts import render, redirect, render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from db.models import Venues, Organizers

def main(request):
    # import pdb; pdb.set_trace()
    # isAuth = False
    # try:
    #     isAuth = request.user.is_authenticated()
    # except:
    #     pass
    context = {
        'venues': Venues.objects.all(),
        'csrf_token': csrf,
        'isAuth': request.user.is_authenticated()
    }
    print context
    return render_to_response('index.html', RequestContext(request,context))
