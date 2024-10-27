from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user_mgmt.views import UsersViewSet

router = DefaultRouter()
router.register('', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]