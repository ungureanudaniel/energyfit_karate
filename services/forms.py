from django import forms
# from .models import Testimonial, ServiceCategory, Service, Contact,\
# Gallery
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class CaptchaForm(forms.Form):
    captcha = CaptchaField()
