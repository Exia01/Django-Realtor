"""
btre URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

# we need to import the settings for the media
from django.conf import settings
# this enables the static
from django.conf.urls.static import static

# This holds the collection for apps urls
urlpatterns = [
    path('', include('apps.pages.urls')),
    path('listing/', include('apps.listings.urls')),
    path('accounts/', include('apps.accounts.urls')),
    # path('realtors/', include('apps.realtors.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
