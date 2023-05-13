from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
import os


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
#================subscribers model=====================================
class About(models.Model):
    main_text = models.TextField()
    what_we_teach1 =  models.CharField(max_length=30)
    what_we_teach2 =  models.CharField(max_length=30)
    what_we_teach3 =  models.CharField(max_length=30)
    what_we_teach4 =  models.CharField(max_length=30)
    about_image = ResizedImageField(size=[1500,None], upload_to='about_images',)
    founder_image = ResizedImageField(size=[640,None], upload_to='founder_images',)
    emphasize_what_we_teach1 = models.CharField(max_length=250)
    emphasize_what_we_teach_icon1 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
    emphasize_what_we_teach2 = models.CharField(max_length=250)
    emphasize_what_we_teach_icon2 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
    emphasize_what_we_teach3 = models.CharField(max_length=250)
    emphasize_what_we_teach_icon3 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
    emphasize_what_we_teach4 = models.CharField(max_length=250)
    emphasize_what_we_teach_icon4 = ResizedImageField(size=[1500,None], upload_to='about_icons',)
    video_link = models.CharField(max_length=300)
    counter_fact1 = models.CharField(max_length=50)
    counter1 = models.IntegerField()
    counter_fact2 = models.CharField(max_length=50)
    counter2 = models.IntegerField()
    counter_fact3 = models.CharField(max_length=50)
    counter3 = models.IntegerField()

    def __str__(self):
        return self.main_text

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
    # thumbnail = ResizedImageField(size=[640,None], upload_to='testimonial_images',)
    text = RichTextField(max_length=400)
    status = models.BooleanField(default="False")
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = "Testimonials"
    def __str__(self):
        return self.email
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
#================Gallery model=====================================
class Gallery(models.Model):
    """
    This class creates database tables for each photo in Energyfit Karate Brasov
    linked to attraction category table above, by ForeignKey. The images for attraction
    will be automatically resized using a package : django-resized. Default settings in
    settings.py file.
    """
    name = models.CharField(max_length=30)
    image = ResizedImageField(size=[640,None], upload_to='attraction_images',)
    text = RichTextField()
    # categ = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
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
    subject = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"
    def __str__(self):
        return '{}'.format(self.email)
#================contact model=====================================
class Training(models.Model):
    """
    This class creates database tables for each training type of
     Energyfit Karate Brasov
    """
    title = models.CharField(max_length=200)
    image = ResizedImageField(size=[640,None], upload_to='training_types_images',)
    icon = ResizedImageField(size=[640,None], upload_to='training_types_icons',)
    first_text = models.TextField()
    second_text = models.TextField()    
    active = models.BooleanField(default=True)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = "Trainings"
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return '{}'.format(self.title)
