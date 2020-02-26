from django.apps import apps
from django.template import VariableDoesNotExist
from cap.apps import DjangoCapConfig


def get_config_instance(app_name=None):
    """
    :rtype: DjangoCapConfig()
    """
    try:
        config = apps.get_app_config(app_name or 'cap')
        if isinstance(config, DjangoCapConfig):
            return config
    except LookupError:
        pass
    return apps.get_app_config('cap')


#: :type: DjangoCapConfig()
cap_config_cls = DjangoCapConfig


def get_config(param=None, request=None):
    cap_config = get_config_instance(get_current_app(request) if request else None)

    # Allow overriding cap config by request
    # Used only for demo purposes
    req_key = '__cap_config_by_request'
    if request and not hasattr(req_key, req_key):
        setattr(request, req_key, True)
        for k, v in request.GET.items():
            if k.startswith('__cap_'):
                setattr(cap_config, k[7:], v)

    if param:
        value = getattr(cap_config, param, None)
        if value is None:
            value = getattr(cap_config_cls, param, None)
        return value

    return cap_config


def get_current_app(request):
    try:
        return request.current_app
    except (VariableDoesNotExist, AttributeError):
        pass
    return None


def set_config_value(name, value):
    config = get_config()
    # Store previous value to reset later if needed
    prev_value_key = '_%s' % name
    if not hasattr(config, prev_value_key):
        setattr(config, prev_value_key, getattr(config, name))
        setattr(config, name, value)


def reset_config_value(name):
    config = get_config()
    prev_value_key = '_%s' % name
    if hasattr(config, prev_value_key):
        setattr(config, name, getattr(config, prev_value_key))
        del config.__dict__[prev_value_key]
