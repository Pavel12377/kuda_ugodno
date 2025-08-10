from django.db import models

NULLABLE = {"blank": True, "null": True}


class TypeFood(models.Model):
    type_of_food = models.CharField(max_length=100, **NULLABLE)
    price = models.CharField(max_length=100, **NULLABLE)

    class Meta:
        ordering = ("id",)


class ListFoodTypes(models.Model):
    type_of_food = models.ForeignKey(TypeFood, on_delete=models.CASCADE)
    without_food = models.BooleanField(
        default=False,
        verbose_name="Без питания",
    )
    breakfast = models.BooleanField(
        default=False,
        verbose_name="Завтрак",
    )
    breakfast_and_dinner = models.BooleanField(
        default=False,
        verbose_name="Завтрак и ужин",
    )
    full_board = models.BooleanField(
        default=False,
        verbose_name="Полный пансион",
    )
    all_inclusive = models.BooleanField(
        default=False,
        verbose_name="All inclusive",
    )
    ultra_all_inclusive = models.BooleanField(
        default=False,
        verbose_name="Ultra All inclusive",
    )
