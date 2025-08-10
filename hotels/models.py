from django.db import models

NULLABLE = {"blank": True, "null": True}


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, db_index=True)
    type_of_holiday = models.CharField(max_length=100, **NULLABLE)
    type_of_accommodation = models.CharField(max_length=100, **NULLABLE)
    country = models.CharField(max_length=100, **NULLABLE)
    latitude = models.CharField(max_length=100, **NULLABLE)
    longitude = models.CharField(max_length=100, **NULLABLE)

    class Meta:
        ordering = ("id",)


class TypeAccommodation(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel = models.BooleanField(
        default=False,
        verbose_name="Отель",
    )
    hostel = models.BooleanField(
        default=False,
        verbose_name="Хостел",
    )
    villa = models.BooleanField(
        default=False,
        verbose_name="Вилла",
    )
    apartments = models.BooleanField(
        default=False,
        verbose_name="Апартаменты",
    )
    guest_house = models.BooleanField(
        default=False,
        verbose_name="Гостевой дом",
    )
