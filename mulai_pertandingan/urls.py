from django.urls import path
from mulai_pertandingan.views import *

app_name = 'mulai_pertandingan'

urlpatterns = [
    path('', show_mulai_pertandingan, name='mulai-pertandingan'),
    path('pilih-peristiwa/1', show_pilih_peristiwa1, name='pilih-peristiwa1'),
    path('pilih-peristiwa/2', show_pilih_peristiwa2, name='pilih-peristiwa2'),
]