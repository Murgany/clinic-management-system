from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns # For localization and translation
from main.views import welcome

# Set up project urls
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls), # Django admin
    path('', include('main.urls')), # The app (Clinic management system)
    path('', include('admin_black.urls')), #An open-source django dashboard that I customised further (files are found in black-admin folder inside venv folder)
)
