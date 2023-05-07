from django.shortcuts import render

# Create your views here.
def show_mulai_rapat(request):
    return render(request, 'mulai_rapat.html')

def show_isi_rapat(request):
    return render(request, 'isi_rapat.html')