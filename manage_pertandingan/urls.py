from django.urls import path
from manage_pertandingan.views import *

app_name = 'manage_pertandingan'

urlpatterns = [
    path('sebelum', show_manage_pertandingan_sebelum, name='manage-pertandingan-sebelum'),
    path('b1', show_manage_pertandingan_b1, name='manage-pertandingan-b1'),
    path('b2', show_manage_pertandingan_b2, name='manage-pertandingan-b2'),
    path('b3', show_manage_pertandingan_b3, name='manage-pertandingan-b3'),
    path('akhir', show_manage_pertandingan_akhir, name='manage-pertandingan-akhir'),
    path('lihat-peristiwa', show_lihat_peristiwa, name='show-lihat-peristiwa'),
]