from django.shortcuts import render

# Create your views here.
def show_manage_pertandingan_sebelum(request):
    return render(request, 'manage_pertandingan_sebelum.html')

def show_manage_pertandingan_b1(request):
    return render(request, 'manage_pertandingan_b1.html')

def show_manage_pertandingan_b2(request):
    return render(request, 'manage_pertandingan_b2.html')

def show_manage_pertandingan_b3(request):
    return render(request, 'manage_pertandingan_b3.html')

def show_manage_pertandingan_akhir(request):
    return render(request, 'manage_pertandingan_akhir.html')

def show_lihat_peristiwa(request):
    return render(request, 'lihat_peristiwa.html')