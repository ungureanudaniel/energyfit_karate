from django.contrib import admin
from .models import ServiceCategory, Testimonial, Contact, Service, Team

class ServiceCategoryAdmin(admin.ModelAdmin):
    fields = ['name_en', 'name_ro', 'name_de', 'image', 'slug']
    prepopulated_fields = {"slug": ("name_en",)}
class ServiceAdmin(admin.ModelAdmin):
    fields = ['name_en', 'name_ro', 'name_de', 'image', 'text_en', 'text_ro', 'text_de', 'categ', 'featured', 'slug']
    prepopulated_fields = {"slug": ("name_en",)}
class TeamAdmin(admin.ModelAdmin):
    fields = ['job_en', 'job_ro', 'job_de', 'text_en', 'text_ro', 'text_de']
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Team, TeamAdmin)
