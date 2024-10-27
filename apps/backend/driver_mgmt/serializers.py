from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from driver_mgmt.models import Driver
from center_mgmt.serializers import CenterMgmtSerializer, CenterNavigationSerializer
from center_mgmt.models import Center

class DriverMgmtSerializer(ModelSerializer):
    centers = CenterMgmtSerializer(many=True, read_only=True)
    class Meta:
        model = Driver
        fields = '__all__'

class DriverLocationSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ['location_lat', 'location_long']
class DriverCenterSerializer(ModelSerializer):
    centers = CenterMgmtSerializer(many=True)
    class Meta:
        model = Driver
        fields = ['centers']

class DriverNavigationSerialzier(ModelSerializer):

    centers = CenterNavigationSerializer(many=True)

    class Meta:

        model = Driver
        fields = ['driver_id', 'lat', 'long', 'centers']
class DriverGreenImpactSerializer(ModelSerializer):

    class Meta:
        model = Driver
        fields = ['driver_id', 'distance_traveled', 'fuel_consumption']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance:
            carbon_fp = float(instance.fuel_consumption)*2.31
            representation['carbon_emission'] = round(carbon_fp,4)

        return representation