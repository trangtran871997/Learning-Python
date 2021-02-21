from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.utils.functional import curry
from asset.filters import DeviceFilter
from asset.models import Device
from asset.models import Management
from asset.pagination import CustomPageNumber
from asset.serializers import DeviceSerializer

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from asset.models import Device
from asset.serializers import DeviceSerializer

@login_required
def main(request):
    return render(request, 'main.html')


def index(request):
    records = DeviceViewSet.as_view({'get': 'get_records'})(request).data
    return render(request, 'index.html', {'data': records})


def customized_logout(request):
    logout(request)
    response = redirect('/asset/main/')
    return response


class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DeviceSerializer
    pagination_class = CustomPageNumber
    queryset = Device.objects.all().order_by('device_id')
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = DeviceFilter
    history = Device.objects.all().order_by('device_id').audit_log.all()

    def get_records(self, request):
        page = self.paginate_queryset(self.history)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(self.history, many=True)
            return Response(serializer.data)



