from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
# import debug_toolbar
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.sitemaps.views import sitemap
from services.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
    # 'snippet': SnippetSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", TemplateView.as_view(template_name="services/robots.txt", content_type="text/plain"),),
    # path('__debug__/', include('debug_toolbar.urls')),

    ]
#
urlpatterns += i18n_patterns(
    path('users/', include('users.urls')),
    path('', include('services.urls')),
    # path('blog', include('blog.urls')),
    path('captcha/', include('captcha.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

