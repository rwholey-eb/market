import urlparse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.template import loader

# import pdb; pdb.set_trace()

def app_login(request):
    user_raw = dict(urlparse.parse_qsl(request.body))
    user_auth = authenticate(username=user_raw['username'], password=user_raw['password'])
    if user_auth is not None:
        if user_auth.is_active:
            login(request, user_auth)
            return redirect('/client/')
        else:
            return HttpResponse('user has been disabled')
    else:
        return redirect_signup(request, user_raw)

def redirect_signup(request, user_raw):
    t = loader.get_template('signup.html')
    return HttpResponse(t.render(user_raw,request))

def app_signup(request):
    user_raw = dict(urlparse.parse_qsl(request.body))
    user = User.objects.create_user(username=user_raw['username'], password=user_raw['password'])
    user_auth = authenticate(username=user_raw['username'], password=user_raw['password'])
    login(request, user_auth)
    return redirect('/client/')

def app_logout(request):
    logout(request)
    return redirect('/client/')




