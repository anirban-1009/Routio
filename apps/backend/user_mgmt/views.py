from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from user_mgmt.models import UserModel
from user_mgmt.serializer import UserSerializer, UserDriverSerializer, UserDriverGreenImpact
from user_mgmt.response_schema import user_driver_response_schema, user_driver_green_impact_response_schema

class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary="List users with optional email filter",
        manual_parameters=[
            openapi.Parameter(
                name="email",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Filter users by email"
            ),
        ],
        responses={
            200: UserSerializer(many=True),
            404: "User not found",
        }
    )
    def list(self, request):
        email = self.request.META['QUERY_STRING'][6:]
        if email:
            user = self.queryset.filter(email=email).first()
            if user:
                serializer = self.get_serializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        serializer = self.get_serializer(self.queryset, many=True)
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

    def partial_update(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['GET'])
    @swagger_auto_schema(
        operation_summary="Get user's driver details",
        responses={
            200: openapi.Response(
                description="User's driver details",
                schema=user_driver_response_schema,
                examples={
                    "application/json": {
                        "user_id": "EFA956B",
                        "center": {
                            "location_lat": 17.51256,
                            "location_long": 78.9870987,
                            "center_id": "CF6F0E5",
                            "level": 0,
                            "ETA": "2021-10-17T15:00:00Z"
                        },
                        "driver": {
                            "driver_id": "aa4289f9e53a4e3484baee7ef5a28834",
                            "location_lat": 21.921337896445223,
                            "location_long": 171.16079816331643
                        }
                    }
                }
            ),
            404: "User not found",
        }
    )
    def driver(self, request, pk=None):
        user = self.get_object()
        serializer = UserDriverSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'], url_path='green-impact', url_name='green-impact')
    @swagger_auto_schema(
        operation_summary="Get user's driver details",
        responses={
            200: openapi.Response(
                description="User's driver details",
                schema=user_driver_green_impact_response_schema,
                examples={
                    "application/json": {
                        "user_id": "EFA956B",
                        "center": "CF6F0E5",
                        "driver": {
                            "driver_id": "aa4289f9e53a4e3484baee7ef5a28834",
                            "distance_traveled": 967.951326988373,
                            "fuel_consumption": 20.709919611486182,
                            "carbon_emission": 47.83991430253308
                        }
                    }
                }
            ),
            404: "User not found",
        }
    )
    def green_impact(self, request, pk=None):
        user = self.get_object()
        serializer = UserDriverGreenImpact(user)
        return Response(serializer.data, status=status.HTTP_200_OK)