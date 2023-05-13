from modeltranslation.translator import translator, TranslationOptions
from .models import ServiceCategory, Service, Trainer, Training, TeamRole, About,\
FAQ


class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
class TrainerTranslationOptions(TranslationOptions):
    fields = ('text', 'job', 'intro', 'experience', 'skill1', 'skill1_descr', 'skill2', 'skill2_descr', 'skill3', 'skill3_descr')
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
class TeamRoleTranslationOptions(TranslationOptions):
    fields = ('title',)
class TrainingTranslationOptions(TranslationOptions):
    fields = ('title', 'first_text', 'second_text')
class AboutTranslationOptions(TranslationOptions):
    fields = ('main_text', 'what_we_teach1', 'what_we_teach2', 'what_we_teach3', 'what_we_teach4', 'emphasize_what_we_teach1', 'emphasize_what_we_teach2', 'emphasize_what_we_teach3', 'emphasize_what_we_teach4', 'counter_fact1', 'counter_fact2', 'counter_fact3')
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'main_explanation', 'subtitle', 'second_text')

translator.register(ServiceCategory, ServiceCategoryTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Trainer, TrainerTranslationOptions)
translator.register(Training, TrainingTranslationOptions)
translator.register(TeamRole, TeamRoleTranslationOptions)
translator.register(About, AboutTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
