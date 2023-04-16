from django.contrib import admin
from .models import ServiceCategory, Testimonial, Contact, Service, Team, Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    fields = ['email', 'conf_num', 'confirmed']
    list_display = ['email', 'conf_num', 'confirmed']
class ServiceCategoryAdmin(admin.ModelAdmin):
    fields = ['rank', 'name', 'name_ro', 'name_de', 'image', 'slug']
    prepopulated_fields = {"slug": ("name",)}
class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'name_ro', 'name_de', 'image', 'text', 'text_ro', 'text_de', 'categ', 'featured', 'slug']
    prepopulated_fields = {"slug": ("name",)}
class TeamAdmin(admin.ModelAdmin):
    fields = ['hierarchy', 'firstname', 'surname', 'image', 'job', 'job_ro', 'job_de', 'text', 'text_ro', 'text_de']
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
