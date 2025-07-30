from rest_framework import serializers

from hotels.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "id",
            "hotel_name",
            "type_of_holiday",
            "type_of_accommodation",
            "country",
            "latitude",
            "longitude",
        )
