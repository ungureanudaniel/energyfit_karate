from django.contrib import admin
from .models import ServiceCategory, Testimonial, Contact, Service, Trainer, Subscriber,\
TeamRole, Training, About, FAQ

class SubscriberAdmin(admin.ModelAdmin):
    fields = ['email', 'conf_num', 'confirmed']
    list_display = ['email', 'conf_num', 'confirmed']
class TestimonialAdmin(admin.ModelAdmin):
    fields = ['fname', 'lname', 'email', 'text', 'status']
    list_display = ['fname', 'lname', 'status']
class ServiceCategoryAdmin(admin.ModelAdmin):
    fields = ['rank', 'name', 'name_ro', 'name_de', 'image', 'slug']
    prepopulated_fields = {"slug": ("name",)}
class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'name_ro', 'name_de', 'image', 'text', 'text_ro', 'text_de', 'categ', 'featured', 'slug']
    prepopulated_fields = {"slug": ("name",)}
class TeamRoleAdmin(admin.ModelAdmin):
    fields = ['title', 'title_ro', 'title_de', 'slug']
    prepopulated_fields = {"slug": ("title",)}
class TrainerAdmin(admin.ModelAdmin):
    fields = ['role', 'firstname', 'surname', 'image', 'job', 'job_ro', 'job_de', 'intro', 'intro_ro', 'intro_de', 'text', 'text_ro', 'text_de', 'experience', 'experience_ro', 'experience_de', 'skill1', 'skill1_ro', 'skill1_de', 'skill1_descr', 'skill1_descr_ro', 'skill1_descr_de', 'skill2', 'skill2_ro', 'skill2_de', 'skill2_descr', 'skill2_descr_ro', 'skill2_descr_de', 'skill3', 'skill3_ro', 'skill3_de', 'skill3_descr', 'skill3_descr_ro', 'skill3_descr_de', 'nr_students', 'training_hours', 'competitions', 'email', 'phone', 'slug']
    prepopulated_fields = {"slug": ("firstname",)}
class TrainingAdmin(admin.ModelAdmin):
    fields = ['title', 'title_ro', 'title_de', 'image', 'icon', 'first_text', 'first_text_ro', 'first_text_de', 'second_text', 'second_text_ro', 'second_text_de', 'active', 'slug']
    prepopulated_fields = {"slug": ("title",)}
class AboutAdmin(admin.ModelAdmin):
    fields = ['main_text', 'main_text_ro', 'main_text_de', 'about_image', 'founder_image', 'what_we_teach1', 'what_we_teach1_ro', 'what_we_teach1_de', 'what_we_teach2', 'what_we_teach2_ro', 'what_we_teach2_de', 'what_we_teach3', 'what_we_teach3_ro', 'what_we_teach3_de', 'what_we_teach4', 'what_we_teach4_ro', 'what_we_teach4_de', 'emphasize_what_we_teach1', 'emphasize_what_we_teach_icon1', 'emphasize_what_we_teach1_ro', 'emphasize_what_we_teach1_de', 'emphasize_what_we_teach2', 'emphasize_what_we_teach_icon2', 'emphasize_what_we_teach2_ro', 'emphasize_what_we_teach2_de', 'emphasize_what_we_teach3', 'emphasize_what_we_teach_icon3', 'emphasize_what_we_teach3_ro', 'emphasize_what_we_teach3_de', 'emphasize_what_we_teach4', 'emphasize_what_we_teach_icon4', 'emphasize_what_we_teach4_ro', 'emphasize_what_we_teach4_de', 'video_link', 'counter_fact1', 'counter1', 'counter_fact1_ro', 'counter_fact1_de', 'counter_fact2', 'counter2', 'counter_fact2_ro', 'counter_fact2_de', 'counter_fact3', 'counter3', 'counter_fact3_ro', 'counter_fact3_de']
class FAQAdmin(admin.ModelAdmin):
    fields = ['question', 'question_ro', 'question_de', 'main_explanation', 'main_explanation_ro', 'main_explanation_de', 'subtitle', 'subtitle_ro', 'subtitle_de', 'second_text', 'second_text_ro', 'second_text_de', 'image1', 'image2', 'image3', 'image4', 'slug']
    prepopulated_fields = {"slug": ("question",)}

admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(TeamRole, TeamRoleAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(FAQ, FAQAdmin)
