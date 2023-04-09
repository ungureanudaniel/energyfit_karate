from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
# from .models import Testimonial, Team, AttractionCategory, Contact,\
# PublicCategory, Attraction, Gallery
from .forms import CaptchaForm
# , ContactForm, GalleryForm
from django.utils.text import slugify
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime
import requests
from django.conf import settings
from django.views.decorators.gzip import gzip_page
from django.utils.translation import gettext_lazy as _
User = get_user_model()

#==================SERVER ERROR 500 HANDLER============================
def handler500(request):
    return render(request, 'services/500.html', status='500')
#========================underconstruction home page=================================
def underconstruction(request):
    """
    This view replaces the home page when website is under construction
    """
    template = 'services/underconstruction.html'
    weather = weather_data()
    context = {
        "weather": weather,
    }
    return render(request, template, context)
#========================underconstruction home page=================================
def home(request):
    """
    This view is the home page view
    """
    template = 'services/home.html'


    context = {
    }
    return render(request, template, context)
#========================about page================================
def team(request):
    template = 'services/team.html'

    context = {
        'dir_members': Team.objects.filter(hierarchy=0),
        'adm_members': Team.objects.filter(hierarchy=1).order_by("surname"),
        'field_members': Team.objects.filter(job__exact="Ranger").order_by("surname"),
    }
    return render(request, template, context)
#========================mass-media page================================
def massmedia(request):
    template = 'services/mass-media.html'
    return render(request, template, {})
#==========contact======================================================
def contacts_view(request):
    template_name = 'services/contact.html'
    if request.method == "POST":
        message_form = ContactForm(request.POST or None)
        form = CaptchaForm(request.POST)
        try:
            if form.is_valid():
                if message_form.is_valid():
                    message_subject = message_form.cleaned_data.get('subject')
                    message_author = message_form.cleaned_data.get('author')
                    sender_email = message_form.cleaned_data.get('email')
                    message = message_form.cleaned_data.get('text')
                    #=======send email=======
                    print(f"{message_subject},{message_author},{sender_email}")
                    new_message = message_form.save(commit=False)
                    new_message.timestamp = datetime.datetime.now()
                    new_message.save()
                    send_mail(message_subject, message, sender_email, ['contact@bucegipark.ro'], fail_silently=False)
                    messages.success(request, _(f'Thank you for writting us {message_author}! We will answer as soon as possible.'))
                    return HttpResponseRedirect('/contact')
                    # except Exception as e:
                    #     messages.warning(request, f'Error: {e}!')
                    #     return render(request, 'services/invalid_header.html',{})
                    # return HttpResponseRedirect('/contact')
                else:
                    messages.warning(request, "Failed! Please make sure your info is correct!")
                    return HttpResponseRedirect('/contact')
            else:
                messages.warning(request, "Failed! Please fill in the captcha field again!")
                return HttpResponseRedirect('/contact')
        except Exception as e:
            messages.warning(request, f"{e}")
    else:
        message_form = ContactForm()
        form = CaptchaForm()
    return render(request, template_name, {'message_form':message_form, 'form': form})
#========================add testimonial page================================
def add_testimonial(request):
    template = 'services/add_testimonial.html'
    if request.method=="POST":
        try:
            fname = request.POST.get('first-name')
            lname = request.POST.get('last-name')
            email = request.POST.get('email')
            image = request.POST.get('image')
            text = request.POST.get('text')


            password = request.POST.get('signin-password')
        except Exception as e:
            messages.warning(request, f"Warning! {e}")
    return render(request, template, {})
#======================== faq page================================
def faq_view(request):
    template = 'services/faq.html'

    context = {
    }
    return render(request, template, context)
#====================== video view ==========================================
def video_view(request):
    template = 'services/videos.html'
    #---------------------fetch YOUTUBE cid IDs-----------------------
    # p_url = 'https://www.googleapis.com/youtube/v3/search'
    # s_url = 'https://www.googleapis.com/youtube/v3/channels'
    # p_params = {
    #     'part': 'snippet',
    #     'channelId': 'UCITVdHG3i6bYsv01X24lBkA',
    #     'type': 'video',
    #     'key': settings.YOUTUBE_DATA_API_KEY,
    # }
    # s_params = {
    #     'part': 'statistics',
    #     'id': 'UCITVdHG3i6bYsv01X24lBkA',
    #     'key': settings.YOUTUBE_DATA_API_KEY,
    # }
    # videos = []
    # s_count = 0
    # url_list = []
    # try:
    #     p_req = requests.get(p_url, params=p_params)
    #     s_req = requests.get(s_url, params=s_params)
    #     p_results = p_req.json()['items']
    #     s_count = s_req.json()['items'][0]['statistics']['subscriberCount']
    #     for p_result in p_results:
    #         video_data = {
    #             'id': p_result['id']['videoId'],
    #             'embed': f'http://www.youtube.com/embed/{ p_result["id"]["videoId"] }',
    #             'url': f'https://www.youtube.com/watch?v={ p_result["id"]["videoId"] }',
    #             'title': p_result['snippet']['title'],
    #             'date': p_result['snippet']['publishedAt'][:4],
    #             'thumbnail':p_result['snippet']['thumbnails']['high']['url'],
    #         }
    #
    #         videos.append(video_data)
    # except Exception as e:
    #     messages.error(request, _('Nereusit!'))
    return render(request, template, {})
#======================== gallery page================================
def gallery(request):
    template = 'services/gallery.html'
    if request.method == "POST":
        gallery_form =  GalleryForm()
        if gallery_form.is_valid():
            new_photo = gallery_form.save()
    else:
        gallery_form =  GalleryForm()
    context = {
    "gallery_form": gallery_form,
    "attr_categ": AttractionCategory.objects.all(),
    "photos":Gallery.objects.all().order_by("name"),
    }
    return render(request, template, context)

#======================== page not found page================================
def page_not_found(request):
    template = 'services/404.html'
    return render(request, template, {})
#======================== invalid header page================================
def invalid_header(request):
    template = 'services/invalid_header.html'
    return render(request, template, {})
#======================== page not found page================================
def coming_soon(request):
    template = 'services/coming-soon.html'
    return render(request, template, {})
