from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    var_nama = "Siti Maemunah"
    contex = {
        "nama":var_nama,
    }
    return render(request, "aplikasi/index.html", contex)

def login(request):
    return render(request, "aplikasi/login.html")