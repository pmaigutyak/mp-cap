
class CapSettings(object):

    @property
    def INSTALLED_APPS(self):

        apps = super().INSTALLED_APPS + [
            'cap',
            'adminplus',
            'django.contrib.admin.apps.SimpleAdminConfig'
        ]

        if 'easy_select2' not in apps:
            apps.append('easy_select2')

        return apps

    @property
    def DATE_INPUT_FORMATS(self):
        return ['%d/%m/%Y'] + super().DATE_INPUT_FORMATS


default = CapSettings
