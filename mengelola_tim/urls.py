from django.urls import path
from mengelola_tim.views import *

app_name = 'mengelola_tim'

urlpatterns = [
    path('', registrasi_tim, name='registrasi_tim'),
    path('tim',tim,name='tim'),
    path('daftar_pemain',daftar_pemain,name='daftar_pemain'),
    path('daftar_pelatih',daftar_pelatih,name='daftar_pelatih')
]