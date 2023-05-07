from django.urls import path
from mulai_rapat.views import show_mulai_rapat, show_isi_rapat
app_name = 'mulai_rapat' 

urlpatterns = [
    path('', show_mulai_rapat, name='show_mulai_rapat'),
    path('rapat', show_isi_rapat, name='show_isi_rapat')
]