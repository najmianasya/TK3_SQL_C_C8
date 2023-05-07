from django.shortcuts import render

# Create your views here.

def membuat_list(request):
    return render(request,'membuat_list.html')


def memilih_stadium(request):
    return render(request,'memilih_stadium.html')

def waktu_stadium(request):
    return render(request,'waktu_stadium.html')

def buat_pertandingan(request):
    return render(request,'buat_pertandingan.html')




