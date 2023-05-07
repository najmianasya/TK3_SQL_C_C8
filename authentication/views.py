from django.shortcuts import render
from django.contrib.auth import logout

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

def landingauth(request):
    return render(request, 'landingauth.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def register_manajer(request):
    return render(request, 'register_manajer.html')

def register_panitia(request):
    return render(request, 'register_panitia.html')

def register_penonton(request):
    return render(request, 'register_penonton.html')


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('dashboard:show_dashboard'))
    #response.delete_cookie('last_login')
    return response
