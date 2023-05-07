from django.shortcuts import render

# Create your views here.

def pembelian(request):
    return render(request,'pembelian.html')


def list_waktu(request):
    return render(request,'list_waktu.html')


def list_pertandingan(request):
    return render(request,'list_pertandingan_beli.html')