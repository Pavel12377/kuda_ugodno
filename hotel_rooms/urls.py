from django.urls import include, path
from rest_framework import routers

from hotel_rooms import views

app_name = "hotel_rooms"

router = routers.DefaultRouter()
router.register("hotel_rooms", views.HotelRoomsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
