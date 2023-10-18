from django.contrib import admin
from .models import ServiceCategory, Testimonial, Contact, Service, Trainer, Subscriber,\
TeamRole, FAQ, Gallery, News, BlogPost, Event, Teaching, Media

class SubscriberAdmin(admin.ModelAdmin):
    fields = ['email', 'conf_num', 'confirmed']
    list_display = ['email', 'conf_num', 'confirmed']
class MediaAdmin(admin.ModelAdmin):
    fields = ['name', 'name_ro', 'link', 'date', 'thumbnail', 'slug',]
    list_display = ['link', 'date', 'slug',]
    prepopulated_fields = {"slug": ("name",)}
class TestimonialAdmin(admin.ModelAdmin):
    fields = ['fname', 'lname', 'email', 'text', 'status']
    list_display = ['fname', 'lname', 'status']
class ServiceCategoryAdmin(admin.ModelAdmin):
    fields = ['rank', 'name', 'name_ro', 'image', 'slug']
    prepopulated_fields = {"slug": ("name",)}
class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'name_ro', 'image', 'text', 'text_ro', 'categ', 'featured', 'slug']
    prepopulated_fields = {"slug": ("name",)}
class TeamRoleAdmin(admin.ModelAdmin):
    fields = ['title', 'title_ro', 'slug']
    prepopulated_fields = {"slug": ("title",)}
class TrainerAdmin(admin.ModelAdmin):
    fields = ['role', 'firstname', 'surname', 'image', 'job', 'job_ro', 'intro', 'intro_ro',\
              'text', 'text_ro', 'experience', 'experience_ro', 'skill1', 'skill1_ro', 'skill1_descr',\
                'skill1_descr_ro', 'skill1_level', 'skill2', 'skill2_ro', 'skill2_descr', 'skill2_descr_ro',\
                    'skill2_level', 'skill3', 'skill3_ro', 'skill3_descr', 'skill3_descr_ro', 'skill3_level',\
                        'nr_students', 'training_hours', 'competitions', 'email', 'phone', 'slug']
    prepopulated_fields = {"slug": ("firstname",)}
class TeachingAdmin(admin.ModelAdmin):
    fields = ['title', 'title_ro', 'image', 'icon','text', 'text_ro', 'active', 'slug']
    prepopulated_fields = {"slug": ("title",)}
# class AboutAdmin(admin.ModelAdmin):
#     fields = ['intro_text_1', 'intro_text_1_ro', 'intro_text_1_de','intro_list_1', 'intro_list_1_ro',\
#             'intro_list_1_de', 'intro_list_2','intro_list_2_ro', 'intro_list_2_de','intro_list_3',\
#             'intro_list_3_ro','intro_list_3_de','intro_list_4','intro_list_4_ro','intro_list_4_de',\
#             'intro_list_5','intro_list_5_ro','intro_list_5_de','intro_list_6','intro_list_6_ro',\
#             'intro_list_6_de','intro_list_7','intro_list_7_ro', 'intro_list_7_de','intro_text_2',\
#             'intro_text_2_ro', 'intro_text_2_de','about_image', 'founder_image', 
#             'what_we_teach1', 'what_we_teach1_ro', 'what_we_teach1_de', 'what_we_teach2', 'what_we_teach2_ro',
#             'what_we_teach2_de','what_we_teach3', 'what_we_teach3_ro','what_we_teach3_de','what_we_teach4',\
#             'what_we_teach4_ro','what_we_teach4_de',\
#             'emphasize_what_we_teach1','emphasize_what_we_teach_icon1', 'emphasize_what_we_teach1_ro',\
#             'emphasize_what_we_teach1_de','emphasize_what_we_teach2', 'emphasize_what_we_teach_icon2',\
#             'emphasize_what_we_teach2_ro',\
#             'emphasize_what_we_teach2_de', 'emphasize_what_we_teach3', 'emphasize_what_we_teach_icon3',\
#             'emphasize_what_we_teach3_ro', 'emphasize_what_we_teach3_de', 'emphasize_what_we_teach4',\
#             'emphasize_what_we_teach_icon4', 'emphasize_what_we_teach4_ro', 'emphasize_what_we_teach4_de',\
#             'video_link', 'counter_fact1', 'counter1', 'counter_fact1_ro', 'counter_fact1_de',\
#             'counter_fact2', 'counter2', 'counter_fact2_ro', 'counter_fact2_de', 'counter_fact3',\
#             'counter3', 'counter_fact3_ro', 'counter_fact3_de', 'counter4', 'counter_fact4',\
#             'counter_fact4_ro', 'counter_fact4_de']
class FAQAdmin(admin.ModelAdmin):
    fields = ['question', 'question_ro', 'main_explanation', 'main_explanation_ro', 'subtitle', 'subtitle_ro', 'second_text', 'second_text_ro', 'image1', 'image2', 'image3', 'image4', 'slug']
    prepopulated_fields = {"slug": ("question",)}
class GalleryAdmin(admin.ModelAdmin):
    fields = ['name', 'name_ro', 'categ','image', 'text', 'text_ro', 'featured', 'slug']
    list_display = ['name',]
    prepopulated_fields = {"slug": ("name",)}
class NewsAdmin(admin.ModelAdmin):
    fields = ['author', 'title','title_ro', 'image', 'text','text_ro','slug']
    prepopulated_fields = {"slug": ("title",)}
class EventAdmin(admin.ModelAdmin):
    fields = ['author', 'categ', 'title','title_ro', 'event_date', 'organizer', 'location', 'image', 'text','text_ro','slug']
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(TeamRole, TeamRoleAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
# admin.site.register(About, AboutAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Teaching, TeachingAdmin)

