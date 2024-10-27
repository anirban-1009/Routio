from django.db import models
import uuid
from driver_mgmt.models import Driver
from center_mgmt.models import Center

def generate_uuid():
    return str(uuid.uuid4())[:7].upper()

class UserModel(models.Model):
    user_id = models.CharField(max_length=7, default=generate_uuid, primary_key=True)
    name = models.CharField(max_length=100, default='Jhon Doe')
    email = models.EmailField(max_length=100, unique=True, null=False)
    address = models.CharField(max_length=200, blank=True, default=None)
    is_driver = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank=True, default=None)
