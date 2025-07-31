from rest_framework import viewsets

from type_of_food.models import TypeFood
from type_of_food.serializers import TypeFoodSerializer


class TypeFoodViewSet(viewsets.ModelViewSet):
    queryset = TypeFood.objects.all()
    serializer_class = TypeFoodSerializer
