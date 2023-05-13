from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from .models import Testimonial, Trainer, ServiceCategory, Service, Contact, Subscriber, TeamRole,\
Training, About, FAQ
from .forms import CaptchaForm, ContactForm
# , GalleryForm
from django.utils.text import slugify
from django.contrib import messages
import random
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime
import requests
from django.conf import settings
from django.db.models import Count
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from hitcount.views import HitCountDetailView
from django.utils import timezone
from django.views.decorators.gzip import gzip_page
from django.utils.translation import gettext_lazy as _
User = get_user_model()
#----------generate unique code for email subscription conf--------------------
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)
#==================SERVER ERROR 500 HANDLER============================
def handler500(request):
    return render(request, 'services/500.html', status='500')
#========================underconstruction home page=================================
@gzip_page
def underconstruction(request):
    """
    This view replaces the home page when website is under construction
    """
    template = 'services/underconstruction.html'
    if request.POST.get('form-type') == "subscribe":
        newsletter_email = request.POST.get('subscriber')
        if newsletter_email:
            try:
                duplicate = Subscriber.objects.get(email=newsletter_email)
                if duplicate:
                    messages.warning(request, _("This email already exists in our database!"))
                    return redirect('/')
            except:
                #-----------------------SAVE IN DATABASE----------------
                sub = Subscriber(email=newsletter_email, conf_num=random_digits(), timestamp=timezone.now())
                sub.save()

                #---------------------send confirmation email settings------
                sub_subject = _("Newsletter Energyfit Karate Brasov")
                from_email='contact@energyfit.ro'
                sub_message = ''
                html_content=_("Thank you for subscribing to our newsletter! You can finalize the process by clicking on this <a style='padding:2px 1px;border:2px solid black' href='{}subscription-confirmation/?email={}&conf_num={}'> button</a>.".format('http://127.0.0.1:8000/', sub.email, sub.conf_num))
                try:
                    send_mail(sub_subject, sub_message, from_email, [sub], html_message=html_content)
                    messages.success(request, _("A confirmation link was sent to your email inbox. Please check!"))
                    return redirect('/')
                except Exception as e:
                    messages.warning(request, e)
                    return redirect('/')
    context = {
    }
    return render(request, template, context)
#========================underconstruction home page=================================
@gzip_page
def home(request):
    """
    This view is the home page view
    """
    if settings.DEVELOPMENT == True:
        template = 'services/underconstruction.html'
    else:
        template = 'services/home.html'
    if request.POST.get('form-type') == "subscribe":
        newsletter_email = request.POST.get('subscriber')
        if newsletter_email:
            try:
                duplicate = Subscriber.objects.get(email=newsletter_email)
                if duplicate:
                    messages.warning(request, _("This email already exists in our database!"))
                    return redirect('/')
            except:
                #-----------------------SAVE IN DATABASE----------------
                sub = Subscriber(email=newsletter_email, conf_num=random_digits(), timestamp=timezone.now())
                sub.save()

                #---------------------send confirmation email settings------
                sub_subject = _("Newsletter Energyfit Karate Brasov")
                from_email='contact@energyfit.ro'
                sub_message = ''
                html_content=_("Thank you for subscribing to our newsletter! You can finalize the process by clicking on this <a style='padding:2px 1px;border:2px solid black' href='{}subscription-confirmation/?email={}&conf_num={}'> button</a>.".format('http://127.0.0.1:8000/', sub.email, sub.conf_num))
                try:
                    send_mail(sub_subject, sub_message, from_email, [sub], html_message=html_content)
                    messages.success(request, _("A confirmation link was sent to your email inbox. Please check!"))
                    return redirect('/')
                except Exception as e:
                    messages.warning(request, e)
                    return redirect('/')
    context = {
        "serv_cats": ServiceCategory.objects.all().order_by('rank'),
        "trainers": Trainer.objects.filter(role=1),
    }
    return render(request, template, context)
#--------------------------------------------------------------subscription_conf
def subscription_conf_view(request):
    template = 'services/subscription_conf.html'

    try:
        sub = Subscriber.objects.get(email=request.GET['email'])
        if sub.conf_num == request.GET['conf_num']:
            try:
                sub.confirmed = True
                sub.save()
            except:
                messages.warning(request, _("Error! Your email cannot be registered. Please contact our IT department at +40 758 039 784"))
            return render(request, template, {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, template, {'email': sub.email, 'action': 'denied'})
    except Exception as e:
        messages.warning(request, e)
        return render(request, template, {})

#---------------------------SUBS DELETION VIEW------------------------------
def unsubscribe(request):
    template = 'services/unsubscribe.html'
    if request.method == "POST":
        unsub_email = request.POST.get('unsub_email')
        if unsub_email:
            try:
                sub = Subscriber.objects.get(email=unsub_email)
                if sub:
                    sub.delete()
                    messages.success(request, _("Success! Unsubscribing was finalized. If you change your mind you can subscribe again anytime"))
                    return render(request, template, {'email': sub.email, 'action': 'unsubscribed'})
                else:
                    messages.warning(request, _("Error! Unsubscribing failed. This email does not exist in our database"))
                    return redirect('/unsubscribe')
            except:
                messages.warning(request, _("Error! Unsubscribing failed. Please contact our IT department at +40 758 039 784"))
                return render(request, template, {'action': 'denied'})
        else:
            messages.warning(request, _("Error! Email incorrect."))
            return render(request, template, {})
    else:
        return render(request, template, {})


#=========================apply page================================
def apply_view(request):
    template = 'services/apply.html'

    context = {

    }
    return render(request, template, context)
#=========================apply page================================
def training_view(request):
    template = 'services/training.html'

    context = {
        't_programs': Training.objects.filter(active=True),
        'about': About.objects.all()[0],
        'faqs': FAQ.objects.all(),
    }
    return render(request, template, context)
#======================== wildlife detail page================================
class TrainingDetailView(DetailView):
    model = Training
    template_name = 'services/training-details.html'
    context_object_name = 'training'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(TrainingDetailView, self).get_context_data(**kwargs)

        context.update({
        # ----------- training programs -------------------------------------------
        't_programs': Training.objects.filter(active=True),
        'form_captcha': CaptchaForm()
        })
        return context
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
    def training(self, request, *args, **kwargs):

        if request.method == "POST":
            form = CaptchaForm(request.POST)
            try:
                if form.is_valid():
                    message_phone = request.GET.get("phone")
                    message_author = request.GET.get("name")
                    sender_email = request.GET.get("email")
                    message = request.GET.get("message")
                    training_type = request.GET.get("training_type")
                    message_subject = f"Registration for {training_type}"
                    #=======send email=======
                    new_message = Contact(message_author, message_phone, sender_email, message_subject, message, timestamp=timezone.now())

                    send_mail("", message, sender_email, ['contact@energyfit.ro'], fail_silently=False)
                    messages.success(request, _(f'Thank you for writing us {message_author}! We will answer as soon as possible.'))
                    return redirect('/')
                    # except Exception as e:
                    #     messages.warning(request, f'Error: {e}!')
                    #     return render(request, 'services/invalid_header.html',{})
                    # return HttpResponseRedirect('/contact')
                else:
                    messages.warning(request, _("Failed! Please fill in the captcha field again!"))
                    return redirect('/contact')
            except Exception as e:
                messages.warning(request, _(f"Forward this error to the page developer: {e}"))
                return redirect('/contact')
        else:
            form = CaptchaForm()

        return self.get(request, *args, **kwargs)

#========================about page================================
def about_view(request):
    template = 'services/about.html'
    context = {
        'trainers': Trainer.objects.filter(role=1),
        'testimonials': Testimonial.objects.all(),
        'about': About.objects.all()[0],
    }
    return render(request, template, context)
#========================mass-media page================================
def trainers_view(request):
    template = 'services/trainers.html'
    return render(request, template, {'trainers':Trainer.objects.all(), 'roles':TeamRole.objects.all()})
#======================== wildlife detail page================================
class TrainersDetailView(DetailView):
    model = Trainer
    template_name = 'services/trainers-details.html'
    context_object_name = 'trainers'
    slug_field = 'slug'


#========================mass-media page================================
def massmedia(request):
    template = 'services/mass-media.html'
    return render(request, template, {})
#==========contact======================================================
def contacts_view(request):
    if settings.DEVELOPMENT == True:
        template_name = 'services/contact_under.html'
    else:
        template_name = 'services/contact.html'

    if request.method == "POST":
        message_form = ContactForm(request.POST or None)
        form = CaptchaForm(request.POST)
        try:
            if form.is_valid():
                if message_form.is_valid():
                    message_phone = message_form.cleaned_data.get('phone')
                    message_author = message_form.cleaned_data.get('author')
                    sender_email = message_form.cleaned_data.get('email')
                    message = message_form.cleaned_data.get('message')
                    #=======send email=======
                    new_message = message_form.save(commit=False)
                    new_message.timestamp = datetime.datetime.now()
                    new_message.save()
                    send_mail("", message, sender_email, ['contact@energyfit.ro'], fail_silently=False)
                    messages.success(request, _(f'Thank you for writing us {message_author}! We will answer as soon as possible.'))
                    return redirect('/contact')
                    # except Exception as e:
                    #     messages.warning(request, f'Error: {e}!')
                    #     return render(request, 'services/invalid_header.html',{})
                    # return HttpResponseRedirect('/contact')
                else:
                    messages.warning(request, _("Failed! Please make sure your info is correct!"))
                    return redirect('/contact')
            else:
                messages.warning(request, _("Failed! Please fill in the captcha field again!"))
                return redirect('/contact')
        except Exception as e:
            messages.warning(request, _(f"Forward this error to the page developer: {e}"))
            return redirect('/contact')
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
            messages.warning(request, _(f"Warning! {e}"))
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
#======================== page not found page================================
def page_not_found(request, exception=None):
    template = 'services/404.html'

    return render(request, 'services/home.html', {})
#======================== page not found page================================
def server_error(request):
    template = 'services/500.html'
    return render(request, template, {})
#======================== privacy page================================
def privacy_view(request):
    template = 'services/privacy.html'
    return render(request, template, {})
#======================== terms page================================
def terms_view(request):
    template = 'services/terms.html'
    return render(request, template, {})
