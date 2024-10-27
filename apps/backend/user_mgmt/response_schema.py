from drf_yasg import openapi

user_driver_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_id': openapi.Schema(type=openapi.TYPE_STRING),
        'center': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'location_lat': openapi.Schema(type=openapi.TYPE_NUMBER),
                'location_long': openapi.Schema(type=openapi.TYPE_NUMBER),
                'center_id': openapi.Schema(type=openapi.TYPE_STRING),
                'level': openapi.Schema(type=openapi.TYPE_INTEGER),
                'ETA': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, nullable=True),
            }
        ),
        'driver': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'driver_id': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DOUBLE),
                'location_lat': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DOUBLE),
                'location_long': openapi.Schema(type=openapi.TYPE_NUMBER),
            }
        ),
    }
)

user_driver_green_impact_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_id': openapi.Schema(type=openapi.TYPE_STRING),
        'center': openapi.Schema(type=openapi.TYPE_STRING),
        'driver': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'driver_id': openapi.Schema(type=openapi.TYPE_STRING),
                'distance_traveled': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                'fuel_consumption': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                'carbon_emission': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
            }
        ),
    }
)

