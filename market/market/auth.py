import urlparse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.template import loader

# import pdb; pdb.set_trace()

def redirect_signup(request, user_raw={}):
    return loadTemplate(request, 'signup.html')

def redirect_login(request):
    return loadTemplate(request, 'login.html')

def loadTemplate(request, template, args={}):
    t = loader.get_template(template)
    return HttpResponse(t.render(args, request))

def app_logout(request):
    logout(request)
    return redirect('/auth/login')

def app_signup(request):
    if (request.method == 'GET'):
        return redirect_signup(request)
    elif (request.method == 'POST'):
        user_raw = dict(urlparse.parse_qsl(request.body))
        if User.objects.get(username=user_raw['username']):
            return loadTemplate(request, 'signup.html', {desired_name_in_use: True})
        user = User.objects.create_user(username=user_raw['username'], password=user_raw['password'])
        user_auth = authenticate(username=user_raw['username'], password=user_raw['password'])
        login(request, user_auth)
        return redirect('/client/')
    else:
        return HttpResponse('Request protocol not supported at auth/signup/')

def app_login(request):
    if (request.method == 'GET'):
        return redirect_login(request)
    elif (request.method == 'POST'):
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
    else:
        return HttpResponse('Request protocol not supported at auth/signup/')
