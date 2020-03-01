
class CapSettings(object):

    @property
    def INSTALLED_APPS(self):
        return [
            'core.configs.CapConfig',
            'adminplus',
            'django.contrib.admin.apps.SimpleAdminConfig'
        ] + super().INSTALLED_APPS
