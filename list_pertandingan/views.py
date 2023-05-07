from django.shortcuts import render
from django.contrib import auth

def list_pertandingan(request):
    return render(request,'list_pertandingan.html')