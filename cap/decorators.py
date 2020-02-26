
from django.template.loader import render_to_string


def short_description(description):

    def decorator(f):

        def wrap(*args, **kwargs):
            return f(*args, **kwargs)

        wrap.short_description = description
        wrap.__name__ = f.__name__

        return wrap

    return decorator


def template_list_item(template_name, description=None):

    def decorator(f):

        def wrap(*args, **kwargs):
            return render_to_string(template_name, f(*args, **kwargs))

        if description is not None:
            wrap.short_description = description

        return wrap

    return decorator
