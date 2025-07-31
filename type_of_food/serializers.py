from rest_framework import serializers

from type_of_food.models import TypeFood


class TypeFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFood
        fields = ("type_of_food", "price")
