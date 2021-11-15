from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def spiderman(request):
    return render(request, 'spiderman.html')

def spiderman_flag(request):
    return HttpResponse("flag{w0rld_w1d3_w3b}")

def spiderman_false_flag(request, false_flag):
    return HttpResponse("Sorry, you just missed Spiderman. He's out crawling the web somewhere else.")

def postmaster(request):
    if request.method == 'GET':
        return render(request, 'postmaster.html')
    elif request.method == "POST":
        return HttpResponse("flag{you_might_call_yourself_POSTmaster_general}")
    return HttpResponse("I don't know what happened...")

def cookie_bar(request):
    response = render(request, 'cookie.html')
    response.set_cookie('flag', 'flag{m&m_choc0late_ch1p_c00kies}', path='/cookie_bar/')
    return response

def indiana_jones(request):
    return render(request, 'jones.html')

def jones_site_raiders(request):
    return render(request, 'site.html', {"title": "Raiders of the Lost Ark (1981)", "image": "/static/images/raiders.jpg"})

def jones_site_doom(request):
    return render(request, 'site.html', {"title": "Indiana Jones and the Temple of Doom (1984)", "image": "/static/images/temple.jpg"})

def jones_site_crusade(request):
    return render(request, 'site.html', {"title": "Indiana Jones and the Last Crusade (1989)", "image": "/static/images/crusade.jpg"})

def jones_site_skull(request):
    return render(request, 'site.html', {"title": "Indiana Jones and the Kingdom of the Crystal Skull (2008)", "image": "/static/images/skull.jpg"})

def jones_site_fifth(request):
    return HttpResponse("flag{beating_a_dead_horse}")

def spaghetti(request):
    return render(request, "spaghetti.html")

def social_insecurity(request):
    return render(request, "social.html", { "message": "Click below to get your new Social Security Number!" })

def social_insecurity_number(request, number):
    if number == 748532557:
        return HttpResponse("flag{its_just_a_random_number}")
    return render(request, "social.html", { "message": "Click below to get your new Social Security Number!", "number": number })

def url_sanitizer(request):
    return render(request, "sanitizer.html", { "message": "Try to get to /sanitizer/flag"})

def url_sanitizer_path(request, path):
    sanitized_path = "Your sanitized path is: /sanitizer/" + path.replace('flag', '')
    return render(request, "sanitizer.html", { "message": sanitized_path })