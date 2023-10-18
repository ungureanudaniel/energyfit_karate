from django.contrib.sitemaps import Sitemap
from .models import Service, Trainer, Gallery
from django.shortcuts import reverse
# from .models import Snippet

class ServicesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Service.objects.all()

    def location(self,obj):
        return '/%s' % (obj.slug)
class TrainerSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Team.objects.all()

    def location(self,obj):
        return '/%s' % (obj.slug)
class GallerySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Gallery.objects.all()

    def location(self,obj):
        return '/%s' % (obj.slug)

class TestimonialSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Testimonial.objects.all()

    def location(self,obj):
        return '/%s' % (obj.slug)
class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['home', 'training',]

    def location(self, item):
        return reverse(item)
#========= sitemap snippet===================
# class SnippetSitemap(Sitemap):
#     def items(self):
#         return Snippet.objects.all()
