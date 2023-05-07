from django.urls import path
from pembelian_tiket.views import *

app_name = 'pembelian_tiket'

urlpatterns = [
    path('',pembelian , name='pembelian'),
    path('list_waktu',list_waktu,name='list_waktu'),
    path('list_pertandingan',list_pertandingan,name='list_pertandingan'),
    path('beli',belitiket,name='belitiket')

]   