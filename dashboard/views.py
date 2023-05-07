from django.shortcuts import render
from django.contrib import auth

# Create your views here.

# def show_dashboard(request):
#     current_user = auth.get_user(request)

#     if(current_user.is_manajer):
#         return render(request, 'dashboard_manajer.html')
#     elif(current_user.is_penonton):
#         return render(request, 'dashboard_penonton.html')
#     elif(current_user.is_panitia):
#         return render(request, 'dashboard_panitia.html')
    
def show_dashboard_manajer(request):
    return render(request, 'dashboard_manajer.html')

def show_dashboard_penonton(request):
    return render(request, 'dashboard_penonton.html')

def show_dashboard_panitia(request):
    return render(request, 'dashboard_panitia.html')