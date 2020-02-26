from django import get_version
from django.apps import AppConfig
from django.contrib.admin.options import ModelAdmin
from . import VERSION

ALL_FIELDS = '__all__'

# Form row sizing as Bootstrap CSS grid classes: (for label, for field column)
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
    django_version = get_version()
    version = VERSION

    # Menu and header layout - horizontal or vertical
    layout = 'horizontal'

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True

    # Define menu
    #: :type: list of cap.menu.ParentItem
    menu = []

    # Automatically add home link
    menu_show_home = True

    # Define callback / handler to change menu before it is getting rendered
    menu_handler = None

    # Enables two column layout for change forms with submit row on the right
    form_submit_on_right = True

    # Hide name/"original" column for all tabular inlines.
    # May be overridden in Inline class by cap_form_inlines_hide_original = False
    form_inlines_hide_original = False

    # For size
    form_size = {
        'default': CAP_FORM_SIZE_X_LARGE,
        # 'fields': {}
        'widgets': {
            'RelatedFieldWidgetWrapper': CAP_FORM_SIZE_XXX_LARGE
        }
        # 'fieldsets': {}
    }

    # form_size setting can be overridden in ModelAdmin using cap_form_size parameter
    #
    # Example:
    # ----------------------------------------------
    # cap_form_size = {
    #     'default': 'col-xs-12 col-sm-2', 'col-xs-12 col-sm-10',
    #     'fields': {
    #          'field_name': CAP_FORM_SIZE_LARGE,
    #          'field_name2': CAP_FORM_SIZE_X_LARGE,
    #      },
    #      'widgets': {
    #          'widget_class_name': CAP_FORM_SIZE_FULL,
    #          'AdminTextareaWidget': CAP_FORM_SIZE_FULL,
    #      },
    #      'fieldsets': {
    #          'fieldset_name': CAP_FORM_SIZE_FULL,
    #          'fieldset_name2': CAP_FORM_SIZE_FULL,
    #      }
    # }

    def __init__(self, app_name, app_module):
        self.setup_model_admin_defaults()
        super().__init__(app_name, app_module)

    def ready(self):
        super().ready()

    def setup_model_admin_defaults(self):
        """
        Override some ModelAdmin defaults
        """
        if self.toggle_changelist_top_actions:
            ModelAdmin.actions_on_top = True
        ModelAdmin.actions_on_bottom = True

        if self.list_per_page:
            ModelAdmin.list_per_page = self.list_per_page
