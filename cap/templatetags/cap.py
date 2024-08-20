from django import template
from django.apps import apps
from django.http import HttpRequest

from cap.menu import MenuManager

register = template.Library()


@register.simple_tag(takes_context=True)
def get_cap_menu(context, request):
    if not isinstance(request, HttpRequest):
        return None
    available_apps = context.get("available_apps")
    if not available_apps:
        return None
    return MenuManager(available_apps, context, request)


@register.simple_tag()
def get_root_categories():
    return apps.get_model("categories", "Category").objects.root_nodes()
