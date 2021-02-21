from django.db import models
from rest_framework.utils import json
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog
from asset.static import *


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
    audit_log = AuditLog()

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
