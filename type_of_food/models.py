from django.db import models

NULLABLE = {"blank": True, "null": True}


class TypeFood(models.Model):
    type_of_food = models.CharField(max_length=100, **NULLABLE)
    price = models.CharField(max_length=100, **NULLABLE)

    class Meta:
        ordering = ("id",)
