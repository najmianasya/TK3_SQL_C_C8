from django.urls import path
from peminjaman_stadium.views import *
app_name = 'peminjaman_stadium' 

urlpatterns = [
    path('', list_pemesanan, name='list_pemesanan'),
    path('peminjaman', peminjaman, name='peminjaman')
]