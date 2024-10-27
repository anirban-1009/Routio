from drf_yasg import openapi

response_schema = {
    "type": "object",
    "properties": {
        "centers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "center_id": {"type": "string"},
                    "location_lat": {"type": "number", "format": "float"},
                    "location_long": {"type": "number", "format": "float"},
                    "date_last_updated": {"type": "string", "format": "date-time"},
                    "ETA": {"type": ["string", "null"]},
                    "in_schedule": {"type": "boolean"},
                    "level": {"type": "integer"},
                    "driver": {"type": "string"}
                },
                "required": ["center_id", "location_lat", "location_long", "date_last_updated", "in_schedule", "level", "driver"]
            }
        }
    },
    "required": ["centers"]
}

response_get_schema_center = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'centers': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'center_id': openapi.Schema(type=openapi.TYPE_STRING),
                    'location_lat': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                    'location_long': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                    'date_last_updated': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    'ETA': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'in_schedule': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    'level': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'driver': openapi.Schema(type=openapi.TYPE_STRING),
                },
                required=['center_id', 'location_lat', 'location_long', 'date_last_updated', 'in_schedule', 'level', 'driver']
            )
        )
    }
)

response_delete_schema_center = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'centers': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'center_id': openapi.Schema(type=openapi.TYPE_STRING),
                    'location_lat': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                    'location_long': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
                    'date_last_updated': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    'ETA': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),  # Nullable field
                    'in_schedule': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    'level': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'driver': openapi.Schema(type=openapi.TYPE_STRING),
                },
                required=[]
            ),
            nullable=True
        )
    }
)

driver_green_impact_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'driver_id': openapi.Schema(type=openapi.TYPE_STRING),
        'distance_traveled': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
        'fuel_consumption': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
        'carbon_emission': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT),
    }
)
