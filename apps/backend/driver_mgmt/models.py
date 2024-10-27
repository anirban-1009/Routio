from django.db import models
import shortuuid

def generate_uuid():
    return shortuuid.ShortUUID().random(length=7).upper()

class Driver(models.Model):
    driver_id = models.CharField(primary_key=True, default=generate_uuid, editable=False, max_length=7)
    email = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=False, default='test_driver@mail.com')
    registration_id = models.CharField(max_length=100, unique=True, null=False, default='PEUWIP0398')
    distance_traveled = models.DecimalField(default=0.0, decimal_places=4, max_digits=100)
    fuel_consumption = models.DecimalField(default=0.0, decimal_places=4, max_digits=100)
    lat = models.FloatField(blank=True, default=None)
    long = models.FloatField(blank=True, default=None)