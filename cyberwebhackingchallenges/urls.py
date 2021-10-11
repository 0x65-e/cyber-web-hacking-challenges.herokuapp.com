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
    path('spiderman/033a76aab1838ba86ec98d952f04fab7', views.spiderman_flag),
    path('postmaster/', csrf_exempt(views.postmaster), name="postmaster"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
