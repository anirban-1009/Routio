from django.urls import include, path
from rest_framework.routers import DefaultRouter
from center_mgmt.views import CenterMgmtViewSet

router = DefaultRouter()
router.register(r'', CenterMgmtViewSet, basename='centers')

urlpatterns = [
    path('', include(router.urls)),
]