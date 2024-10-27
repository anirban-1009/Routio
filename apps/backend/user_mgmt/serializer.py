from rest_framework.serializers import ModelSerializer
from user_mgmt.models import UserModel
from center_mgmt.serializers import CenterLocationSerializer

class UserSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = UserModel

class UserDriverSerializer(ModelSerializer):

    center = CenterLocationSerializer()

    class Meta:
        fields = ['user_id', 'center']
        model = UserModel

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['driver'] = {}
        if instance.center.driver:
            representation['driver']['driver_id'] = instance.center.driver.driver_id
            representation['driver']['lat'] = instance.center.driver.lat
            representation['driver']['long'] = instance.center.driver.long

        return representation

class UserDriverGreenImpact(ModelSerializer):

    class Meta:
        fields = ['user_id', 'center']
        model = UserModel

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['driver'] = {}
        if instance.center.driver:
            representation['driver']['driver_id'] = (instance.center.driver.driver_id)
            representation['driver']['distance_traveled'] = round(instance.center.driver.distance_traveled, 4)
            representation['driver']['fuel_consumption'] = round(instance.center.driver.fuel_consumption, 4)
            carbon_fp = int(instance.center.driver.fuel_consumption)*2.31
            representation['driver']['carbon_emission'] = round(carbon_fp,4)

        return representation