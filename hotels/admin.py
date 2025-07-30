from django.contrib import admin

from hotels.models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "hotel_name",
        "type_of_holiday",
        "type_of_accommodation",
        "country",
        "latitude",
        "longitude",
    )
    list_display_links = ("hotel_name",)
    list_filter = ("hotel_name",)
