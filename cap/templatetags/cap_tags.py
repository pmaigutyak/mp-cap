
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from cap import config

register = template.Library()


@register.filter(name='cap_conf')
def cap_conf(name, request):
    value = config.get_config(name, request)
    return mark_safe(value) if isinstance(value, str) else value


@register.filter(name='cap_body_class')
def cap_body_class(value, request):
    css_classes = []
    config_vars_to_add = ['toggle_changelist_top_actions', 'form_submit_on_right', 'layout']
    for each in config_vars_to_add:
        cap_conf_param = getattr(config.get_config(None, request), each, None)
        if cap_conf_param:
            value = each if isinstance(cap_conf_param, bool) \
                else '_'.join((each, cap_conf_param))
            css_classes.append('cap_%s' % value)
    return ' '.join(css_classes)


@register.simple_tag(takes_context=True)
def get_core_settings(context):
    if context.request.user.is_staff:
        return settings
    return {}