from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API.viewsets import BurgerViewSet

router = DefaultRouter()
router.register(r"burgers", BurgerViewSet, basename="burgers")

urlpatterns = [
    path("", include(router.urls)),
]
