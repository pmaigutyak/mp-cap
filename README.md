
### Installation:
* add rows to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    "cap",
    "django.contrib.admin.apps.SimpleAdminConfig",
    ...
]
```
* add row to root `urls`
```python
from django.contrib import admin

admin.autodiscover()

urlpatterns = [  # or i18n_patterns
    path('admin/', admin.site.urls),
    ...
]
```
