
### Installation:
* add rows to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    'cap',
    'cap.configs.SuitConfig',
    'django.contrib.admin.apps.SimpleAdminConfig',
    ...
]
```
* add row to root `urls`
```python
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [  # or i18n_patterns
    path('admin/', admin.site.urls),
    ...
]
```
