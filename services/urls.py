from django.urls import path, include
from django.conf import settings
from .views import home
#, gallery, add_testimonial, team, history, massmedia,\
 # contacts_view, underconstruction, page_not_found, coming_soon, public_docs,\
 # scraped_data, wildlife, flora, invalid_header, faq_view, video_view, gallery
#, snippet_detail
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from users.views import user_logout, user_login

if settings.DEVELOPMENT == False:
    urlpatterns = [
        #-------Authentication----------------
        path('login/', user_login, name='login'),
        path('logout/', user_logout, name='logout'),
        #-------sitemap snippet link-----------
        # path('<slug:slug>', snippet_detail),
        #------ general urls-------------------
        path('', underconstruction, name="underconstruction"),
        # path('gallery', gallery, name="gallery"),
        # path('team', team, name="team"),
        # path('mass-media', massmedia, name="mass-media"),
        # path('_(frequently-asked-questions)', flora, name="flora"),
        # path('', home, name="home"),
        # path('contact', contacts_view, name="contact"),
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
        # path('gallery', gallery, name="gallery"),
        # path('team', team, name="team"),
        # path('mass-media', massmedia, name="mass-media"),
        # path('_(frequently-asked-questions)', flora, name="flora"),
        # path('contact', contacts_view, name="contact"),
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
