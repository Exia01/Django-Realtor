"""
btre URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
# This holds the collection for apps urls

urlpatterns = [
    path('', include('apps.pages.urls')),
    path('admin/', admin.site.urls),
]
