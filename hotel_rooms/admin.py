from django.contrib import admin

from hotel_rooms.models import HotelRoom


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = (
        "room_category",
        "type_of_food",
        "adults_living",
        "children_living",
        "area",
        "number_of_rooms_category",
    )
    list_display_links = ("room_category",)
    list_filter = ("room_category",)
