from django.shortcuts import render, redirect
from django.http import HttpResponse
from db.models import Venues, Organizers

import urlparse

def venues(request):
    if request.method == 'POST':
        return venue_post(request)
    elif request.method == 'GET':
        return HttpResponse('GET HAPPENED to Venue')
    else:
        return HttpResponse('DEFAULT to Venue')

def organizers(request):
    if request.method == 'POST':
        return HttpResponse('POST to Organizer')
    elif request.method == 'GET':
        return HttpResponse('GET to Organizer')
    else:
        return HttpResponse('DEFAULT to Organizer')

def string_to_number(string):
    try:
        return int(string)
    except ValueError:
        print 'Number not passed for capacity'
        return 0

def venue_post(request):
    import pdb; pdb.set_trace()
    venue_obj = dict(urlparse.parse_qsl(request.body))
    v = Venues(
        name=venue_obj['name'],
        location=venue_obj['location'],
        capacity=string_to_number(venue_obj['capacity']),
    )
    v.save()
    return redirect('/client/')

