from rest_framework import serializers

from hotel_rooms.models import HotelRoom


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = (
            "id",
            "room_category",
            "type_of_food",
            "adults_living",
            "children_living",
            "number_of_rooms_category",
        )
