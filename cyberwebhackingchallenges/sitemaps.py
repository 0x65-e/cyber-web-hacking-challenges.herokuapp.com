from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'never'

    def items(self):
        return ['index', 'spiderman', 'postmaster', 'cookie-bar', 'jones', 'raiders', 'temple', 'crusade', 'skull', 'untitled', 'spaghetti', 'social-insecurity', 'url-sanitizer', 'telescope', 'robot-detection']

    def location(self, item):
        return reverse(item)