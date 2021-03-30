
from django.conf import settings
from django.forms import DateInput, TextInput
from easy_select2.widgets import Select2Multiple, Select2


class DatePickerInput(DateInput):

    def __init__(self, attrs=None, format=None):

        if format is None:
            format = settings.DATE_INPUT_FORMATS[0]

        if attrs is None:
            attrs = {}

        attrs['data-role'] = 'datepicker'

        super().__init__(attrs=attrs, format=format)


class TagsInput(TextInput):

    def __init__(self, attrs=None):

        if attrs is None:
            attrs = {}

        attrs['data-role'] = 'tagsinput'

        super().__init__(attrs=attrs)


class Select(Select2):
    pass


class SelectMultiple(Select2Multiple):
    pass
