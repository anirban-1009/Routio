from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from driver_mgmt.serializers import (
    DriverMgmtSerializer,
    DriverLocationSerializer,
    DriverCenterSerializer,
    DriverGreenImpactSerializer,
    DriverNavigationSerialzier
)
from driver_mgmt.response_schema import (
    response_get_schema_center,
    response_delete_schema_center,
    driver_green_impact_response_schema
)
from driver_mgmt.models import Driver
from center_mgmt.models import Center

class DriverViewSet(ModelViewSet):
    serializer_class = DriverMgmtSerializer
    queryset = Driver.objects.all()

    def list(self, request):
        email = self.request.META['QUERY_STRING'][6:]
        if email:
            user = self.queryset.filter(email=email).first()
            if user:
                serializer = self.get_serializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        driver = self.get_object()
        serializer = self.get_serializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        driver = self.get_object()
        serializer = self.get_serializer(driver, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        driver = self.get_object()
        serializer = self.get_serializer(driver, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        driver = self.get_object()
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'location_lat': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'location_long': openapi.Schema(type=openapi.TYPE_INTEGER),
                    },
                ),
                examples={
                    'application/json': {
                        'data': {
                            'location_lat': 21.921337896445223,
                            'location_long': 171.11631643,
                        }
                    }
                }
            ),
            404: "Driver not found",
            403: "Permission Denied"
        }
    )
    def location(self, request, pk=None):
        driver = self.get_object()
        serializer = DriverLocationSerializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def navigate(self, request, pk=None):
        driver = self.get_object()
        serializer = DriverNavigationSerialzier(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method='GET', responses={200: response_get_schema_center})
    @swagger_auto_schema(method='PATCH', responses={200: response_get_schema_center})
    @swagger_auto_schema(method='DELETE', responses={200: response_delete_schema_center})
    @action(detail=True, methods=['GET', 'PATCH', 'DELETE'])
    def centers(self, request, pk=None):
        if request.method == 'GET':
            driver = self.get_object()
            serializer = DriverCenterSerializer(driver)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'PATCH':
            driver = self.get_object()
            serializer = DriverCenterSerializer(driver)
            for center in request.data['centers']:
                try:
                    center = Center.objects.get(center_id=center)
                except Center.DoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                center.driver = driver
                center.in_schedule = True
                center.save()
            return Response(serializer.data)

        if request.method == 'DELETE':
            driver = self.get_object()
            driver.centers.clear()
            serializer = DriverCenterSerializer(driver)

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    @swagger_auto_schema(
        operation_summary="Get Driver's green impact",
        responses={
            200: openapi.Response(
                description="User's driver details",
                schema=driver_green_impact_response_schema,
                examples={
                    "application/json": {
                        "driver_id": "aa4289f9e53a4e3484baee7ef5a28834",
                        "distance_traveled": 967.9513,
                        "fuel_consumption": 20.7099,
                        "carbon_emission": 47.8399
                    }
                }
            ),
            404: "User not found",
        }
    )
    @action(detail=True, methods=['GET'], url_name='green-impact', url_path='green-impact')
    def green_impact(self, request, pk=None):
        driver = self.get_object()
        serializer = DriverGreenImpactSerializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)
