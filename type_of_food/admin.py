from django.contrib import admin

from type_of_food.models import TypeFood


@admin.register(TypeFood)
class TypeFoodAdmin(admin.ModelAdmin):
    list_display = ("type_of_food", "price")
    list_display_links = ("type_of_food",)
    list_filter = ("type_of_food",)
