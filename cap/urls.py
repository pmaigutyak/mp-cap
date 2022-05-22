
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


if hasattr(settings, 'SITE_HEADER'):
    admin.site.site_header = settings.SITE_HEADER

admin.autodiscover()


app_urls = i18n_patterns(

    path('admin/', admin.site.urls),

    path("select2/", include("django_select2.urls")),

)
