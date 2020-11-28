
from django.urls import path
from django.contrib import admin
from django.utils.module_loading import autodiscover_modules
from adminplus.sites import AdminSitePlus


class AdminSite(AdminSitePlus):

    def get_urls(self):
        urls = super().get_urls()

        for path_str, view, name, urlname, visible in self.custom_views:
            urls = [
                path(path_str, self.admin_view(view), name=urlname),
            ] + urls
        return urls


def register_admin(site_header='Admin'):
    site = AdminSite()
    admin.site = site
    admin.sites.site = site
    admin.site.site_header = site_header
    autodiscover_modules('admin', register_to=site)
