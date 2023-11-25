from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
import os
from django.contrib.auth.models import User
from django.utils import timezone
#================subscribers model=====================================
class FAQ(models.Model):
    question = models.CharField(max_length=100)
    main_explanation =  models.TextField()
    subtitle = models.CharField(max_length=30, blank=True)
    second_text =  models.TextField(null=True, blank=True)
    image1 = ResizedImageField(size=[640,None], upload_to='faq_images')
    image2 = ResizedImageField(size=[640,None], upload_to='faq_images', blank=True)
    image3 = ResizedImageField(size=[640,None], upload_to='faq_images', blank=True)
    image4 = ResizedImageField(size=[640,None], upload_to='faq_images', blank=True)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.slug
#=================media model===================================
class Media(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = ResizedImageField(size=[640,None], upload_to='media_images')
    date = models.DateTimeField()
    link = models.URLField(max_length = 300)
    slug = models.SlugField(max_length=300, allow_unicode=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.slug
#================subscribers model=====================================
# class About(models.Model):
#     intro_text_1 = models.TextField()
#     intro_list_1 =  models.CharField(max_length=100)
#     intro_list_2 =  models.CharField(max_length=100)
#     intro_list_3 =  models.CharField(max_length=100)
#     intro_list_4 =  models.CharField(max_length=100)
#     intro_list_5 =  models.CharField(max_length=100)
#     intro_list_6 =  models.CharField(max_length=100)
#     intro_list_7 =  models.CharField(max_length=100)
#     intro_text_2 = models.TextField()
#     about_image = ResizedImageField(size=[1500,None], upload_to='about_images',)
#     founder_image = ResizedImageField(size=[640,None], upload_to='founder_images',)
#     what_we_teach1 = models.CharField(max_length=50)
#     what_we_teach2 = models.CharField(max_length=50)
#     what_we_teach3 = models.CharField(max_length=50)
#     what_we_teach4 = models.CharField(max_length=50)
#     emphasize_what_we_teach1 = models.CharField(max_length=250)
#     emphasize_what_we_teach_icon1 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
#     emphasize_what_we_teach2 = models.CharField(max_length=250)
#     emphasize_what_we_teach_icon2 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
#     emphasize_what_we_teach3 = models.CharField(max_length=250)
#     emphasize_what_we_teach_icon3 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
#     emphasize_what_we_teach4 = models.CharField(max_length=250)
#     emphasize_what_we_teach_icon4 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
#     video_link = models.CharField(max_length=300)
#     counter_fact1 = models.CharField(max_length=50)
#     counter1 = models.IntegerField()
#     counter_fact2 = models.CharField(max_length=50)
#     counter2 = models.IntegerField()
#     counter_fact3 = models.CharField(max_length=50)
#     counter3 = models.IntegerField()
#     counter_fact4 = models.CharField(max_length=50)
#     counter4 = models.IntegerField()

#     def __str__(self):
#         return self.intro_text_1

#================subscribers model=====================================
class Subscriber(models.Model):
    email = models.EmailField(max_length=200)
    conf_num =  models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
#================testimonial model=====================================
class Testimonial(models.Model):
    """
    This class creates database tables for each testimonial given on the page of
     Energyfit Karate Brasov
    """
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    text = models.TextField(max_length=500)
    status = models.BooleanField(default="False")
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = "Testimonials"
    def __str__(self):
        return self.email
#================results model=====================================
class Results(models.Model):
    """
    This class creates database tables for each result of
     Energyfit Karate Brasov
    """
    title = models.CharField(max_length=30)
    icon = ResizedImageField(size=[640,None], upload_to='results_icons',)
    details = models.TextField(max_length=500)
    date = models.DateTimeField()
    class Meta:
        verbose_name = 'Results'
        verbose_name_plural = "Results"
    def __str__(self):
        return self.title
#================Attraction category models=====================================
class ServiceCategory(models.Model):
    """
    This class creates database tables for categories for each service in
    Energyfit Karate Brasov
    """
    name = models.CharField(max_length=100)
    image = ResizedImageField(size=[640,None], upload_to='servicecategory_images',)
    rank = models.IntegerField()
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)

    class Meta:
        verbose_name = 'Service Category'
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#================Attraction model=====================================
class Service(models.Model):
    """
    This class creates database tables for each service in Energyfit Karate Brasov
    linked to service category table above, by ForeignKey. The images for services
    will be automatically resized using a package : django-resized. Default settings in
    settings.py file.
    """
    name = models.CharField(max_length=100)
    image = ResizedImageField(size=[640,None], upload_to='service_images',)
    text = RichTextField()
    categ = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
#================gallery category model=====================================
# class GalleryCategory(models.Model):
#     """
#     This class creates database tables for categories for each gallery item in
#     Energyfit Karate Brasov
#     """
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)

#     class Meta:
#         verbose_name = 'Pictures Category'
#         verbose_name_plural = "Picture Categories"

#     def __str__(self):
#         return self.slug
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#================Gallery model=====================================
class Gallery(models.Model):
    """
    This class creates database tables for each photo in Energyfit Karate Brasov
    linked to attraction category table above, by ForeignKey. The images for attraction
    will be automatically resized using a package : django-resized. Default settings in
    settings.py file.
    """
    CATEG_CHOICES = (
            (_('training'), _('training')),
            (_('competitions'), _('competitions')),
            (_('other'), _('other')),
        )
    name = models.CharField(max_length=30)
    image = ResizedImageField(size=[640,None], upload_to='attraction_images',)
    text = RichTextField()
    categ = models.CharField(choices=CATEG_CHOICES, max_length=50)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = "Gallery"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
#================Team Role model=====================================
class TeamRole(models.Model):
    """
    This class creates database tables for each role category in the team.

    """
    title = models.CharField(max_length=30)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
#================Team model=====================================
class Trainer(models.Model):
    """
    This class creates database tables for each masters of energyfit karate. The
    thumbnails will be automatically resized using a package : django-resized.

    """
    surname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    image = ResizedImageField(size=[640,None], upload_to='team_images',)
    phone = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    intro = models.CharField(max_length=500)
    text = RichTextField()
    skill1 = models.CharField(max_length=50)
    skill1_descr = models.TextField()
    skill1_level = models.IntegerField()
    skill2 = models.CharField(max_length=50)
    skill2_descr = models.TextField()
    skill2_level = models.IntegerField()
    skill3 = models.CharField(max_length=50)
    skill3_descr = models.TextField()
    skill3_level = models.IntegerField()
    experience = models.TextField()
    nr_students = models.IntegerField()
    training_hours = models.IntegerField()
    competitions = models.IntegerField()
    role = models.ForeignKey(TeamRole, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=10)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = "Trainers"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname + "-" + self.surname)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.surname}" + " " + f"{self.firstname}"

#================contact model=====================================
class Contact(models.Model):
    """
    This class creates database tables for each contact message send from contact page of
     Energyfit Karate Brasov
    """
    author = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50, default="No subject")
    text = models.TextField(max_length=300)
    timestamp = models.DateTimeField(default=timezone.now())
    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = "Messages"
    def __str__(self):
        return '{}'.format(self.email)
#================weekdays model=====================================
class WeekDays(models.Model):
    """
    This class creates database tables for each contact message send from contact page of
     Energyfit Karate Brasov
    """
    name = models.CharField(max_length=9)
    
    class Meta:
        verbose_name = 'Week Days'
        verbose_name_plural = "Week Days"
    def __str__(self):
        return '{}'.format(self.name)
#================training program model=====================================
class TrainingSchedule(models.Model):
    """
    This class creates database tables for each training schedule program of
     Energyfit Karate Brasov
    """
    day = models.ForeignKey(WeekDays, on_delete=models.CASCADE)
    # day = models.CharField(max_length=100)
    training1 = models.CharField(max_length=100, blank=True, null=True)
    training2 = models.CharField(max_length=100, blank=True, null=True)
    training3 = models.CharField(max_length=100, blank=True, null=True)
    starting_time1 = models.TimeField(blank=True, null=True)
    ending_time1 = models.TimeField(blank=True, null=True)
    starting_time2 = models.TimeField(blank=True, null=True)
    ending_time2 = models.TimeField(blank=True, null=True)
    starting_time3 = models.TimeField(blank=True, null=True)
    ending_time3 = models.TimeField(blank=True, null=True)
    class Meta:
        verbose_name = _('Training Schedule')
        verbose_name_plural = _('Training Schedule')
    def __str__(self):
        return '{}'.format(self.day)
#================event model=====================================
class Event(models.Model):
    """
    This class creates database tables for each event of
     Energyfit Karate Brasov
    """
    # CATEG_CHOICES = (
    #         (_('past'), _('past')),
    #         (_('future'), _('future')),
    #     )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.CharField(max_length=200)
    image = ResizedImageField(size=[640,None], upload_to='event_images',)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    text = RichTextField(max_length=1000)
    # categ = models.CharField(choices=CATEG_CHOICES, max_length=50)
    event_date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('event-details', args=[self.slug])
    def __str__(self):
        return '{}'.format(self.slug)
#================blog model=====================================
class BlogPost(models.Model):
    """
    This class creates database tables for each blog post of
     Energyfit Karate Brasov
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.CharField(max_length=200)
    image = ResizedImageField(size=[640,None], upload_to='blog_images',)
    title = models.CharField(max_length=100)
    text = RichTextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = "Blog Posts"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('blogpost-details', args=[self.slug])
    def __str__(self):
        return '{}'.format(self.slug)
#================blog model=====================================
class News(models.Model):
    """
    This class creates database tables for each blog post of
     Energyfit Karate Brasov
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = ResizedImageField(size=[640,None], upload_to='news_images',)
    title = models.CharField(max_length=100)
    text = RichTextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('news-details', args=[self.slug])
    def __str__(self):
        return '{}'.format(self.slug)
#================moves model=====================================
class Teaching(models.Model):
    """
    This class creates database tables for each teaching type of
     Energyfit Karate Brasov
    """
    title = models.CharField(max_length=200)
    image = ResizedImageField(size=[640,None], upload_to='teachings_images',)
    icon = ResizedImageField(size=[640,None], upload_to='teachings_icons',)
    text = models.TextField()
    active = models.BooleanField(default=True)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Teaching'
        verbose_name_plural = "Teachings"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return '{}'.format(self.title)
