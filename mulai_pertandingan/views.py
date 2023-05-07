from django.shortcuts import render

# Create your views here.
def show_mulai_pertandingan(request):
    return render(request, 'mulai_pertandingan.html')

def show_pilih_peristiwa1(request):
    return render(request, 'pilih_peristiwa1.html')

def show_pilih_peristiwa2(request):
    return render(request, 'pilih_peristiwa2.html')