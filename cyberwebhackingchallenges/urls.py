"""cyberwebhackingchallenges URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('spiderman/', views.spiderman, name='spiderman'),
    path('spiderman/033a76aab1838ba86ec98d952f04fab7/', views.spiderman_flag),
    path('spiderman/<str:false_flag>/', views.spiderman_false_flag),
    path('postmaster/', csrf_exempt(views.postmaster), name="postmaster"),
    path('cookie_bar/', views.cookie_bar, name="cookie-bar"),
    path('jones/', views.indiana_jones, name="jones"),
    path('jones/raiders_of_the_lost_ark/', views.jones_site_raiders, name="raiders"),
    path('jones/temple_of_doom/', views.jones_site_doom, name="temple"),
    path('jones/last_crusade/', views.jones_site_crusade, name="crusade"),
    path('jones/kingdom_of_the_crystal_skull/', views.jones_site_skull, name="skull"),
    path('jones/untitled/', views.jones_site_fifth, name="untitled"),
    path('spaghetti/', views.spaghetti, name="spaghetti"),
    path('social_insecurity/', views.social_insecurity, name="social-insecurity"),
    path('social_insecurity/<int:number>', views.social_insecurity_number),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sanitizer/', views.url_sanitizer, name="url-sanitizer"),
    path('sanitizer/<str:path>', views.url_sanitizer_path),
    path('telescope/', views.json_web_telescope, name="telescope"),
    path('robot_detection/', views.robot_detection, name="robot-detection"),
]
