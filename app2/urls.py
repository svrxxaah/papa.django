from django.urls import path
from .views import home, faq, contact

urlpatterns = [
    path('', home, name='app2_home'),
    path('faq/', faq, name='app2_faq'),
    path('contact/', contact, name='app2_contact'),
]
