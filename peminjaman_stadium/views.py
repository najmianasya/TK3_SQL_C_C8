from django.shortcuts import render

# Create your views here.
def list_pemesanan(request):
    return render(request,'list_pemesanan.html')

def peminjaman(request):
    return render(request,'peminjaman.html')
