
from django.apps import AppConfig
from django.contrib.admin.options import ModelAdmin

ALL_FIELDS = '__all__'

CAP_FORM_SIZE_LABEL = 'col-xs-12 col-sm-3 col-md-2'
CAP_FORM_SIZE_INLINE = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-9 col-md-10 form-inline')
CAP_FORM_SIZE_SMALL = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-6 col-md-5 col-lg-4')
CAP_FORM_SIZE_HALF = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-7 col-md-6 col-lg-5')
CAP_FORM_SIZE_LARGE = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-8 col-md-7 col-lg-6')
CAP_FORM_SIZE_X_LARGE = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-9 col-md-8 col-lg-7')
CAP_FORM_SIZE_XX_LARGE = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-9 col-md-10 col-lg-8')
CAP_FORM_SIZE_XXX_LARGE = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-9 col-md-10 col-lg-9')
CAP_FORM_SIZE_FULL = (CAP_FORM_SIZE_LABEL, 'col-xs-12 col-sm-9 col-md-10')


class DjangoCapConfig(AppConfig):

    name = 'cap'
    verbose_name = 'Django Cap'

    layout = 'vertical'

    list_per_page = 20

    toggle_changelist_top_actions = True

    menu = []

    menu_show_home = True

    form_submit_on_right = True

    form_inlines_hide_original = False

    form_size = {
        'default': CAP_FORM_SIZE_X_LARGE,
        'widgets': {
            'RelatedFieldWidgetWrapper': CAP_FORM_SIZE_XXX_LARGE
        }
    }

    def __init__(self, app_name, app_module):
        self.setup_model_admin_defaults()
        super().__init__(app_name, app_module)

    def ready(self):
        super().ready()

    def setup_model_admin_defaults(self):

        if self.toggle_changelist_top_actions:
            ModelAdmin.actions_on_top = True
        ModelAdmin.actions_on_bottom = True

        if self.list_per_page:
            ModelAdmin.list_per_page = self.list_per_page
