from django import forms
from .models import Contact, Testimonial
# Gallery
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class CaptchaForm(forms.Form):
    captcha = CaptchaField()

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['style'] = "width:100%;margin:0 20px 20px 0px;"
        self.fields['email'].widget.attrs['style'] = "width:100%;margin:0 20px 20px 0px;"
        self.fields['phone'].widget.attrs['style'] = "width:100%;margin-bottom:10px;"
        self.fields['subject'].widget.attrs['style'] = "width:100%;margin-left: 0;height:300px"
        self.fields['text'].widget.attrs['style'] = "width:100%;margin-left: 0;height:300px"

    class Meta:
        model = Contact
        fields = ['author', 'email', 'phone', 'subject', 'text']
        widgets = {
            'author': forms.TextInput(attrs = {'class': 'col-xl-12 form--control', 'placeholder': _('Full name...')}),
            'email': forms.EmailInput(attrs = {'class': 'col-xl-12 form--control', 'placeholder': 'Email...'}),
            'phone': forms.TextInput(attrs = {'class': 'col-xl-12 form--control', 'placeholder': _('Phone number...')}),
            'subject': forms.TextInput(attrs= {'class': 'col-xl-12 form--control', 'placeholder': _('Subject...')}),
            'text': forms.TextInput(attrs= {'class': 'col-xl-12 form--control', "style": "width:400px;",'placeholder': _('Your message...')}),


        }

class TestimonialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs['style'] = "width:100%;margin:0 20px 20px 0px;"
        self.fields['lname'].widget.attrs['style'] = "width:100%;margin:0 20px 20px 0px;"
        self.fields['email'].widget.attrs['style'] = "width:100%;margin-bottom:10px;"
        self.fields['text'].widget.attrs['style'] = "margin-left: 0;width:100%;height:300px"
    class Meta:
        model = Testimonial
        fields = ['fname', 'lname', 'email', 'text']
        widgets = {
            'fname': forms.TextInput(attrs = {'class': 'form--control', 'placeholder': _('First name...')}),
            'lname': forms.TextInput(attrs = {'class': 'form--control', 'placeholder': _('Last name...')}),
            'email': forms.EmailInput(attrs = {'class': 'form--control', 'placeholder': 'Email...'}),
            'text': forms.TextInput(attrs= {'class': 'form--control', 'placeholder': _('Your message...')}),


        }
