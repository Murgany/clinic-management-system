from django.urls import path
from .views import welcome
urlpatterns = [
    path('', welcome, name='welcome'),
    # path('i18n/', include('django.conf.urls.i18n')),
   ]
