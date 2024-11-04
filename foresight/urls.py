# Imported Files and Packages
from django.contrib import admin
from django.urls import path, include
# Foresight URL paths
urlpatterns = [
    path('', include('social.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
