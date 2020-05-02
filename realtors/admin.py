from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    """ To show the required fields on admin panel """
    list_display = ('id', 'name', 'email')  # To display field names
    list_display_links = ('id', 'name')  # To make clickable links
    search_fields = ('name',)  # Searchable fields
    list_per_page = 25  # Fot listing per page


admin.site.register(Realtor, RealtorAdmin)
