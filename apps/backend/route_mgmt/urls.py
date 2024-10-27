from django.urls import include, path
from rest_framework.routers import DefaultRouter
from route_mgmt.views import RouteMgmtViewset

router = DefaultRouter()
router.register('', RouteMgmtViewset, basename='routes')

urlpatterns = [
    path('', include(router.urls))
]