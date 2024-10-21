from django.urls import path
from .views import home, about, services

urlpatterns = [
    path('', home, name='app1_home'),
    path('about/', about, name='app1_about'),
    path('services/', services, name='app1_services'),
]
