"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('auth/',include('authentication.urls')),
    path('history',include('history_rapat.urls')),
    path('mulai-pertandingan/',include('mulai_pertandingan.urls')),
    path('mulai_rapat/',include('mulai_rapat.urls')),
    path('list_pertandingan',include('list_pertandingan.urls')),
    path('pembelian_tiket/',include('pembelian_tiket.urls')),
    path('peminjaman_stadium/',include('peminjaman_stadium.urls')),
<<<<<<< HEAD
    path('pembuatan_pertandingan/',include('pembuatan_pertandingan.urls')),
    path('mengelola_tim/',include('mengelola_tim.urls'))
=======
    path('manage-pertandingan/', include('manage_pertandingan.urls'))
>>>>>>> 2f769ba004fc83a228ec96f84b22db4c608365d2
]
