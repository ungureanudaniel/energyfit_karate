from django import forms
# from .models import Testimonial, ServiceCategory, Service, Contact,\
# Gallery
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class CaptchaForm(forms.Form):
    captcha = CaptchaField()

# class ServiceCatForm(forms.ModelForm):
#     class Meta:
#         model = ServiceCategory
#         fields = ['name', 'image']
#         widgets = {
#             'name': forms.TextInput(attrs = {'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class':'form-control', 'type':'hidden',}),
#         }
# attr_choices = ServiceCategory.objects.all().values_list('name_en', 'name_en')
#
# attr_choices_list = []
#
# for item in attr_choices:
#     attr_choices_list.append(item)
# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Service
#         fields = '__all__'
#         # fields = ['name', 'image', 'text', 'categ', 'slug']
#         # exclude = ('slug',)
#         widgets = {
#             'name': forms.TextInput(attrs = {'class': 'form-control'}),
#             'text': CKEditorWidget(config_name='default'),
#             'categ': forms.Select(choices=attr_choices_list, attrs = {'class': 'form-control'}),
#         }
