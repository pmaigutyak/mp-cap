
from django import template
from cap.config import get_config


register = template.Library()


@register.simple_tag(takes_context=True)
def cap_form_conf(context, param_name, inline_admin_formset=None):
    """
    Get form config param
    """
    if inline_admin_formset:
        model_admin = inline_admin_formset.opts
    else:
        model_admin = context['adminform'].model_admin
    param_by_model_admin = getattr(model_admin, 'cap_%s' % param_name, None)
    if param_by_model_admin is not None:
        return param_by_model_admin
    return get_config(param_name, context['request'])
