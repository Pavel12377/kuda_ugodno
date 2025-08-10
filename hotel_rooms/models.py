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


class ListCategoryRoom(models.Model):
    room_category = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    standard = models.BooleanField(
        default=False,
        verbose_name="Standard",
    )
    single_room = models.BooleanField(
        default=False,
        verbose_name="Single Room",
    )
    double_room = models.BooleanField(
        default=False,
        verbose_name="Double Room",
    )
    twin_room = models.BooleanField(
        default=False,
        verbose_name="Twin Room",
    )
    triple_room = models.BooleanField(
        default=False,
        verbose_name="Triple Room",
    )
    family_room = models.BooleanField(
        default=False,
        verbose_name="Family Room",
    )
    superior_room = models.BooleanField(
        default=False,
        verbose_name="Superior Room",
    )
    deluxe_room = models.BooleanField(
        default=False,
        verbose_name="Deluxe Room",
    )
    studio = models.BooleanField(
        default=False,
        verbose_name="Studio",
    )
    suite = models.BooleanField(
        default=False,
        verbose_name="Suite",
    )
    junior_suite = models.BooleanField(
        default=False,
        verbose_name="Junior Suite",
    )
    residence = models.BooleanField(
        default=False,
        verbose_name="Residence",
    )
    royal_suite = models.BooleanField(
        default=False,
        verbose_name="Royal Suite",
    )
    penthouse = models.BooleanField(
        default=False,
        verbose_name="Penthouse",
    )
