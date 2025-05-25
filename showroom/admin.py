#from django.contrib import admin
#from .models import Bike
#admin.site.register(Bike)

from django.contrib import admin
from django.utils.html import format_html
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock', 'image_tag')  # Show image preview
    readonly_fields = ('image_tag',)  # So image shows in detail page too

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" />', obj.image.url)
        return "No Image"

    image_tag.short_description = 'Image'

