
from django.urls import path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


app_urls = i18n_patterns(

    path('admin/', admin.site.urls)

)
