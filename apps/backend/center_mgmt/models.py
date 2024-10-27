from django.db import models
import uuid
from driver_mgmt.models import Driver

def generate_uuid():
    return str(uuid.uuid4())[:7].upper()
class Center(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['lat', 'long'], name='unique_lat_long_center')
        ]

    center_id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=7)
    lat = models.FloatField()
    long = models.FloatField()
    date_last_updated = models.DateTimeField(blank=True, default=None)
    ETA = models.DateTimeField(blank=True, default=None)
    in_schedule = models.BooleanField(default=False)
    quantity = models.IntegerField(choices=[
        (0, 'Low'),
        (50, 'Mid'),
        (100, 'High')
    ], default=0)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='centers', blank=True, default=None)
