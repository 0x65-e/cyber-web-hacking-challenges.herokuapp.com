from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def spiderman(request):
    return render(request, 'spiderman.html')

def spiderman_flag(request):
    return HttpResponse(r"flag{w0rld_w1d3_w3b}")