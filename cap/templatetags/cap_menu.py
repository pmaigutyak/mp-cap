
from django import template
from django.http import HttpRequest

from cap.menu import MenuManager

register = template.Library()


@register.simple_tag(takes_context=True)
def get_menu(context, request):

    if not isinstance(request, HttpRequest):
        return None

    available_apps = context.get('available_apps')

    return MenuManager(available_apps, context, request)
