from django import forms
from .models import Contact
# Gallery
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class CaptchaForm(forms.Form):
    captcha = CaptchaField()

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['author', 'email', 'phone', 'subject', 'text']
        widgets = {
            'author': forms.TextInput(attrs = {'class': 'form__field', 'placeholder': _('Full name...')}),
            'email': forms.EmailInput(attrs = {'class': 'form__field', 'placeholder': 'Email...'}),
            'phone': forms.TextInput(attrs = {'class': 'form__field', 'placeholder': _('Phone number...')}),
            'subject': forms.TextInput(attrs= {'class': 'form__field', 'placeholder': _('Subject...')}),
            'text': forms.TextInput(attrs= {'class': 'form__field form__message', 'placeholder': _('Your message...')}),


        }
