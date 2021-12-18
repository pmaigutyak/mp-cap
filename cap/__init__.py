
from django.conf.global_settings import DATE_INPUT_FORMATS


def setup_settings(settings, **kwargs):

    settings['INSTALLED_APPS'] += [
        app for app in [
            'cap.configs.SuitConfig',
            'django.contrib.admin.apps.SimpleAdminConfig',
            'adminplus',
            'easy_select2'
        ] if app not in settings['INSTALLED_APPS']
    ]

    if 'DATE_INPUT_FORMATS' not in settings:
        settings['DATE_INPUT_FORMATS'] = DATE_INPUT_FORMATS

    date_format = '%d/%m/%Y'

    if date_format not in settings['DATE_INPUT_FORMATS']:
        settings['DATE_INPUT_FORMATS'].append(date_format)
