from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    #path('', show_dashboard, name='show_dashboard'),
    path('manajer/', show_dashboard_manajer, name='show_dashboard_manajer'),
    path('penonton/', show_dashboard_penonton, name='show_dashboard_penonton'),
    path('panitia/', show_dashboard_panitia, name='show_dashboard_panitia'),
]