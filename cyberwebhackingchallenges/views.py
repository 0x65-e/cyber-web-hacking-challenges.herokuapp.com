from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def spiderman(request):
    return render(request, 'spiderman.html')

def spiderman_flag(request):
    return HttpResponse("flag{w0rld_w1d3_w3b}")

def postmaster(request):
    if request.method == 'GET':
        return render(request, 'postmaster.html')
    elif request.method == "POST":
        return HttpResponse("flag{you_might_call_yourself_POSTmaster_general}")
    return HttpResponse("I don't know what happened...")