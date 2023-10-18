from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import home, apply_view, underconstruction, contacts_view, subscription_conf_view,\
unsubscribe, about_view, TrainersDetailView, trainers_view, training_view,\
events_view, EventDetailView, blog_view, BlogDetailView, gallery, news_view, NewsDetailView,\
pricing_view, faq_view, coming_soon, media_view, program_view, donate_view
#, gallery, add_testimonial, team, history, massmedia,\
 # contacts_view, page_not_found, coming_soon,\
 #, video_view, gallery
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
        path('about', about_view, name="about"),
        path('', underconstruction, name="underconstruction"),
        path('subscription-confirmation/', subscription_conf_view, name='subscription-confirmation'),
        path('unsubscribe', unsubscribe, name='unsubscribe'),
        path("apply-now", apply_view, name="apply"),
        path('trainer-details/<slug:slug>/', TrainersDetailView.as_view(), name='trainer-details'),
        path("trainers", trainers_view, name="trainers"),
        path("training", training_view, name="training"),
        path("training-schedule", program_view, name="training-schedule"),
        path('events', events_view, name="events"),
        path('event-details/<slug:slug>', EventDetailView.as_view(), name="event-details"),
        path('blogposts', blog_view, name="events"),
        path('blogpost-details/<slug:slug>', BlogDetailView.as_view(), name="blog-details"),
        path('gallery', gallery, name="gallery"),
        path('news', news_view, name="news"),
        path('news-details/<slug:slug>', NewsDetailView.as_view(), name="news-details"),
        path('pricing-plan', pricing_view, name="pricing"),
        path('frequently-asked-questions', faq_view, name="faqs"),
        path('mass-media', media_view, name="media"),
        path('contact', contacts_view, name="contact"),
        path('support-us', donate_view, name="donate"),

        # path('videos', video_view, name="video"),
        path('coming-soon', coming_soon, name="coming-soon"),
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
        path('about', about_view, name="about"),
        path("trainers", trainers_view, name="trainers"),
        path('trainers-details/<slug:slug>/', TrainersDetailView.as_view(), name='trainers-details'),
        path("training", training_view, name="training"),
        path("training-schedule", program_view, name="training-schedule"),
        path('mass-media', media_view, name="media"),
        path('contact', contacts_view, name="contact"),
        path('events', events_view, name="events"),
        path('event-details/<slug:slug>', EventDetailView.as_view(), name="event-details"),
        path('blogposts', blog_view, name="blog"),
        path('blogpost-details/<slug:slug>', BlogDetailView.as_view(), name="blogpost-details"),
        path('gallery', gallery, name="gallery"),
        path('news', news_view, name="news"),
        path('news-details/<slug:slug>', NewsDetailView.as_view(), name="news-details"),
        path('pricing-plan', pricing_view, name="pricing"),
        path('frequently-asked-questions', faq_view, name="faqs"),
        path('support-us', donate_view, name="donate"),

        # path('videos', video_view, name="video"),
        path('coming-soon', coming_soon, name="coming-soon"),
        # path('scraped-data', scraped_data, name="scraped_data"),
        #--------error pages -------------------
        # path('invalid-header', invalid_header, name="invalid_header"),
        # path('404', page_not_found, name="page_not_found"),
        ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
