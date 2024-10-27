from rest_framework.serializers import ModelSerializer
from center_mgmt.models import Center

class CenterMgmtSerializer(ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'

class CenterLocationSerializer(ModelSerializer):
    class Meta:
        model = Center
        fields = ['lat', 'long', 'center_id', 'quantity', 'ETA']

class CenterNavigationSerializer(ModelSerializer):

    class Meta:

        model = Center
        fields = ['center_id', 'lat', 'long']