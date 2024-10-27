from route_mgmt.models import Route
from rest_framework.serializers import ModelSerializer

class RouteMgmtSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'