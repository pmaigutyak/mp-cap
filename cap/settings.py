
class CapSettings(object):

    @property
    def INSTALLED_APPS(self):
        return [
            'cap',
            'adminplus',
            'django.contrib.admin.apps.SimpleAdminConfig'
        ] + super().INSTALLED_APPS

    @property
    def DATE_INPUT_FORMATS(self):
        return ['%d/%m/%Y'] + super().DATE_INPUT_FORMATS


default = CapSettings
