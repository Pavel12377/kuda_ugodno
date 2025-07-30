from rest_framework import viewsets

from hotels.models import Hotel
from hotels.serializers import HotelSerializer


class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
