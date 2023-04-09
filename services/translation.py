from modeltranslation.translator import translator, TranslationOptions
from .models import ServiceCategory, Service, Team


class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
class TeamTranslationOptions(TranslationOptions):
    fields = ('text', 'job')
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
translator.register(ServiceCategory, ServiceCategoryTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Team, TeamTranslationOptions)
