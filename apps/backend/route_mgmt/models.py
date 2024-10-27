from django.db import models
import shortuuid
from driver_mgmt.models import Driver

def route_id():
    return shortuuid.ShortUUID().random(length=7)
class Route(models.Model):
    """
        This model defines how the routes will be stored, they will have a unique ID assigned to them.
        They will be assigned to a driver each.
    """
    route_id = models.CharField(max_length=7, unique=True, default=route_id, primary_key=True)
    result = models.JSONField()  # Stores polyline data as JSON
