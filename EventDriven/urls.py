from django.contrib import admin
from django.urls import path, include
from .views import landing_page  # Import the landing page view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),  # Add landing page URL
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
]
