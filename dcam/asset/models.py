import datetime
from django.db import models
from rest_framework.utils import json
from simple_history.models import HistoricalRecords
from django.utils import timezone
from asset.static import *
#from auditlog.registry import auditlog


def serialize_class(obj):
    att_dict = {}
    for attribute, value in obj.__dict__.items():
        if not attribute.startswith('_') \
                and not attribute.startswith('id') \
                and value:
            att_dict[attribute] = str(value)
    return json.dumps(att_dict)


class Device(models.Model):
    device_id = models.CharField(max_length=CONFIG_DEVICE_ID_MAX_LEN, primary_key=True)
    name = models.CharField(max_length=CONFIG_NAME_MAX_LEN)
    description = models.CharField(max_length=1024, blank=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=16,
                              choices=STATUS_CHOICES,
                              default=STATUS_CHOICES.__getitem__(0))
    note = models.CharField(max_length=2048, blank=True)

    def __str__(self):
        return serialize_class(self)


class Change(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='asset_device', )
    changed_field = models.CharField("field_name")
    changed_data = models.TextField()  # you can improve this by storing the data in compressed format
    changed_at = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def __str__(self):
        return serialize_class(self)


class Management(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='management',)
    owner = models.CharField(max_length=32)
    zone = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    request_code = models.CharField(max_length=CONFIG_NAME_MAX_LEN, blank=True)
    parent_device = models.CharField(max_length=CONFIG_DEVICE_ID_MAX_LEN, blank=True)

    def __str__(self):
        return serialize_class(self)


class License(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='license')
    name = models.CharField(max_length=CONFIG_NAME_MAX_LEN)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return serialize_class(self)


class Product(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return serialize_class(self)


class Warranty(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return serialize_class(self)
