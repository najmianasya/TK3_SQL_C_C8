from django.urls import path
from authentication.views import landingauth,login,register,register_manajer,register_panitia,register_penonton,logout_user

app_name = 'authentication'

urlpatterns = [
    path('', landingauth, name='auth'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('register/panitia',register_panitia,name='register_panitia'),
    path('register/manajer',register_manajer,name='register_manajer'),
    path('register/penonton',register_penonton,name='register_penonton'),
    path('logout/', logout_user, name='logout'),
]