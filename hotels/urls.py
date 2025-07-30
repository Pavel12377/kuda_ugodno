from django.urls import include, path
from rest_framework import routers

from hotels import views

app_name = "hotels"

router = routers.DefaultRouter()
router.register("hotels", views.HotelsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
