from django.contrib import admin

# importing listing model
from .models import Listing

admin.site.register(Listing)