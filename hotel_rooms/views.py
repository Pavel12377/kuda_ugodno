from rest_framework import viewsets

from hotel_rooms.models import HotelRoom
from hotel_rooms.serializers import HotelRoomSerializer


class HotelRoomsViewSet(viewsets.ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
