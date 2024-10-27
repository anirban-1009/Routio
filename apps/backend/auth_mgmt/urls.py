from django.urls import include, path
from rest_framework.routers import DefaultRouter
from auth_mgmt.views import TokenViewset

router = DefaultRouter()
router.register(r'token', TokenViewset, basename='drivers')

urlpatterns = [
    path('', include(router.urls))
]
