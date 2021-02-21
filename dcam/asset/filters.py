from _warnings import filters

import django_filters
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from asset.models import Device
from asset.models import Management
from asset.pagination import CustomPageNumber
from asset.serializers import DeviceSerializer


# class DeviceFilter(django_filters.rest_framework.FilterSet):
#     u = django_filters.rest_framework.CharFilter(name='name', lookup_expr='exact')
#     u__contains = django_filters.rest_framework.CharFilter(name='name', lookup_expr='contains')
#
#     class Meta:
#         model = Device
#         fields = ['u', 'u__contains']

class DeviceFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Device
        fields = {
            "name": ["exact", "contains"],
            "status": ["exact"]
        }
