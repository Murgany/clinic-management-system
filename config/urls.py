from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),
#     path('', include('admin_black.urls')),
# ]

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
 
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('admin_black.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('admin_tools_stats/', include('admin_tools_stats.urls')),
    # path('rosetta/', include('rosetta.urls')),
    # If no prefix is given, use the default language
    # prefix_default_language=False
)