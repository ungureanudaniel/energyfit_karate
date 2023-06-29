from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import home, apply_view, underconstruction, contacts_view, subscription_conf_view,\
unsubscribe, about_view, TrainersDetailView, trainers_view, training_view, TrainingDetailView,\
events_view
#, gallery, add_testimonial, team, history, massmedia,\
 # contacts_view, page_not_found, coming_soon,\
 # faq_view, video_view, gallery
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from users.views import user_logout, user_login

if settings.DEVELOPMENT == True:
    urlpatterns = [
        #-------Authentication----------------
        path('login/', user_login, name='login'),
        path('logout/', user_logout, name='logout'),
        #-------sitemap snippet link-----------
        # path('<slug:slug>', snippet_detail),
        #------ general urls-------------------
        path('home', home, name="home"),
        path('', underconstruction, name="underconstruction"),
        path('subscription-confirmation/', subscription_conf_view, name='subscription-confirmation'),
        path('unsubscribe', unsubscribe, name='unsubscribe'),
        path("apply-now", apply_view, name="apply"),
        path('trainer-details/<slug:slug>/', TrainersDetailView.as_view(), name='trainer-details'),
        path("trainers", trainers_view, name="trainers"),

        # path('gallery', gallery, name="gallery"),
        # path('team', team, name="team"),
        # path('mass-media', massmedia, name="mass-media"),
        # path('_(frequently-asked-questions)', flora, name="flora"),
        # path('', home, name="home"),
        path('contact', contacts_view, name="contact"),
        # path('gallery', gallery, name="gallery"),
        # path('videos', video_view, name="video"),
        # path('coming-soon', coming_soon, name="coming-soon"),
        # path('scraped-data', scraped_data, name="scraped_data"),
        #--------error pages -------------------
        # path('invalid-header', invalid_header, name="invalid_header"),
        # path('404', page_not_found, name="page_not_found"),
        ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        #-------Authentication----------------
        path('login/', user_login, name='login'),
        path('logout/', user_logout, name='logout'),
        #-------sitemap snippet link-----------
        # path('<slug:slug>', snippet_detail),
        #------ general urls-------------------
        path('', home, name="home"),
        path('subscription-confirmation/', subscription_conf_view, name='subscription-confirmation'),
        path('unsubscribe', unsubscribe, name='unsubscribe'),
        path("apply-now", apply_view, name="apply"),
        # path('gallery', gallery, name="gallery"),
        path('about', about_view, name="about"),
        path("trainers", trainers_view, name="trainers"),
        path('trainers-details/<slug:slug>/', TrainersDetailView.as_view(), name='trainers-details'),
        path("training", training_view, name="training"),
        path("training-details/<slug:slug>/", TrainingDetailView.as_view(), name="training_details"),
        # path('mass-media', massmedia, name="mass-media"),
        # path('_(frequently-asked-questions)', flora, name="flora"),
        path('contact', contacts_view, name="contact"),
        path('events', events_view, name="events"),

        # path('gallery', gallery, name="gallery"),
        # path('videos', video_view, name="video"),
        # path('coming-soon', coming_soon, name="coming-soon"),
        # path('scraped-data', scraped_data, name="scraped_data"),
        #--------error pages -------------------
        # path('invalid-header', invalid_header, name="invalid_header"),
        # path('404', page_not_found, name="page_not_found"),
        ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
