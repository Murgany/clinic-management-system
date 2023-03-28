from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from main.views import welcome

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('admin_black.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

    # If no prefix is given, use the default language
    # prefix_default_language=False
)

# urlpatterns = [
    # path('', welcome, name='welcome'),
    # path('i18n/', include('django.conf.urls.i18n')),
#    ]