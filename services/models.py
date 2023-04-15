from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
import os

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
    thumbnail = ResizedImageField(size=[640,None], upload_to='testimonial_images',)
    text = RichTextField(max_length=300)
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
#================Team model=====================================
class Team(models.Model):
    """
    This class creates database tables for each masters of energyfit karate. The
    thumbnails will be automatically resized using a package : django-resized.

    """
    surname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    image = ResizedImageField(size=[640,None], upload_to='team_images',)
    phone = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    text = RichTextField()
    hierarchy = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = "Team members"

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
