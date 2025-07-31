from django.db import models

NULLABLE = {"blank": True, "null": True}


class HotelRoom(models.Model):
    room_category = models.CharField(max_length=100, **NULLABLE)
    type_of_food = models.CharField(max_length=100, **NULLABLE)
    adults_living = models.PositiveIntegerField(**NULLABLE)
    children_living = models.PositiveIntegerField(**NULLABLE)
    area = models.PositiveIntegerField(**NULLABLE)
    number_of_rooms_category = models.PositiveIntegerField(**NULLABLE)

    class Meta:
        ordering = ("id",)
