from django.urls import include, path
from rest_framework.routers import DefaultRouter
from driver_mgmt.views import DriverViewSet

router = DefaultRouter()
router.register(r'', DriverViewSet, basename='drivers')

urlpatterns = [
    path('', include(router.urls))
]