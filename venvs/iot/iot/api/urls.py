from rest_framework import routers
from api.views import SensorViewSet
from django.urls import path, include
router = routers.DefaultRouter()
router.register('sensor', SensorViewSet)
urlpatterns = [
  path('', include(router.urls)),
]