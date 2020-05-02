from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    """ To show the required fields on admin panel """
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')  # To display  field names
    list_display_links = ('id', 'title')  # To make clickable link (title)
    list_filter = ('realtor',)  # To filter according to the realtors
    list_editable = ('is_published',)  # To make it editable (CheckBox)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')  # This will create search
    # box where we can search keyword from the fileds mentioned.
    list_per_page = 25  # For listings per page


admin.site.register(Listing, ListingAdmin)
