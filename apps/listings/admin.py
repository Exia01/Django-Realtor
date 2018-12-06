from django.contrib import admin

from .models import Listing

# This class changes how the listings will be display on admin 
class ListingAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    # Renders the content with an href
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)  #comma since it is a tuple?
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


# importing listing model and passing the ListingAdmin class
admin.site.register(Listing, ListingAdmin)
