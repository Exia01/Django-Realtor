from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25


# importing the admin model and class above
admin.site.register(Realtor, RealtorAdmin)
