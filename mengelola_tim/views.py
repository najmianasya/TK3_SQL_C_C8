from django.shortcuts import render
from django.contrib import auth

def registrasi_tim(request):
    return render(request,'registrasi_tim.html')

def tim(request):
    return render(request,'tim.html')

def daftar_pemain(request):
    return render(request,'daftarpemain.html')

def daftar_pelatih(request):
    return render(request,'daftarpelatih.html')