from django.urls import path
from pembuatan_pertandingan.views import *

app_name = 'pembuatan_pertandingan'

urlpatterns = [
    path('',membuat_list , name='list'),
    path('stadium',memilih_stadium,name='stadium'),
    path('waktu',waktu_stadium,name='waktu'),
    path('buat',buat_pertandingan,name='buat_pertandingan')
]