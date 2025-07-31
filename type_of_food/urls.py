from django.urls import include, path
from rest_framework import routers

from type_of_food import views

app_name = "type_of_food"

router = routers.DefaultRouter()
router.register("type_of_food", views.TypeFoodViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
