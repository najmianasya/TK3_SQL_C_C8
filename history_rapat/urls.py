from django.urls import path
from history_rapat.views import history
app_name = 'history_rapat' 

urlpatterns = [
    path('', history, name='history'),

]