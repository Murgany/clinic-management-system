from django.urls import path
from .views import welcome

# set up landing page url
urlpatterns = [
    path('', welcome, name='welcome'),
   ]

