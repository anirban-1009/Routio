from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from center_mgmt.models import Center
from center_mgmt.serializers import CenterLocationSerializer, CenterMgmtSerializer


class CenterMgmtViewSet(ModelViewSet):
    serializer_class = CenterMgmtSerializer
    queryset = Center.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        center = self.get_object()
        serializer = self.get_serializer(center)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        center = self.get_object()
        serializer = self.get_serializer(center, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        center = self.get_object()

        center.delete()
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
                        'center_id': openapi.Schema(type=openapi.TYPE_STRING),
                        'level': openapi.Schema(type=openapi.TYPE_NUMBER)
                    },
                ),
                examples={
                    'application/json': {
                        'data': {
                            'location_lat': 17.51256,
                            'location_long': 78.9870987,
                            'center_id': '335EAD6',
                            'level': 0,
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'application/json': {
                            'detail': openapi.Schema(type=openapi.TYPE_INTEGER),
                        }
                    },
                ),
                examples={
                    'application/json': {
                        'detail': 'No Center matches the given query.'
                    }
                }
            ),
            403: "Permission Denied"
        }
    )
    def location(self, request, pk=None):
        center = self.get_object()
        serializer = CenterLocationSerializer(center)
        return Response(serializer.data, status=status.HTTP_200_OK)
