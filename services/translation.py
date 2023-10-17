from modeltranslation.translator import translator, TranslationOptions
from .models import ServiceCategory, Service, Trainer, TeamRole,\
FAQ, Gallery, News, BlogPost, Event, Teaching, Media


class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
class MediaTranslationOptions(TranslationOptions):
    fields = ('name',)
class TrainerTranslationOptions(TranslationOptions):
    fields = ('text', 'job', 'intro', 'experience', 'skill1', 'skill1_descr', 'skill2', 'skill2_descr', 'skill3', 'skill3_descr')
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
class TeamRoleTranslationOptions(TranslationOptions):
    fields = ('title',)
class TeachingTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)
# class AboutTranslationOptions(TranslationOptions):
#     fields = ('intro_text_1', 'intro_list_1', 'intro_list_2','intro_list_3','intro_list_4',\
#             'intro_list_5','intro_list_6','intro_list_7', 'intro_text_2', 'what_we_teach1', 'what_we_teach2',\
#             'what_we_teach3', 'what_we_teach4', 'emphasize_what_we_teach1','emphasize_what_we_teach2',\
#             'emphasize_what_we_teach3', 'emphasize_what_we_teach4',\
#             'counter_fact1', 'counter_fact2', 'counter_fact3', 'counter_fact4')
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'main_explanation', 'subtitle', 'second_text')
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
translator.register(ServiceCategory, ServiceCategoryTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Trainer, TrainerTranslationOptions)
translator.register(Teaching, TeachingTranslationOptions)
translator.register(TeamRole, TeamRoleTranslationOptions)
# translator.register(About, AboutTranslationOptions)
translator.register(Gallery, GalleryTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(BlogPost, BlogPostTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Media, MediaTranslationOptions)
