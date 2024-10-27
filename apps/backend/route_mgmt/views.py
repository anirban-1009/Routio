from route_mgmt.models import Route
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from route_mgmt.serializers import RouteMgmtSerializer

class RouteMgmtViewset(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteMgmtSerializer


    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            route = Route.objects.get(route_id=pk)
        except Route.DoesNotExist:
            return Response({"error": "Route not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(route)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        route = self.get_object()
        serializer = self.get_serializer(route, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        route = self.get_object()
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
