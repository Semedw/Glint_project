from django.urls import path

from core.views import (
    home, services
    )



urlpatterns = [
    path('', home, name='home'),
    path('services/<slug:slug>', services, name='services'),

]