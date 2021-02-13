from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from asset.models import Device
from asset.pagination import CustomPageNumber
from asset.serializers import DeviceSerializer


def index(request):
    records = DeviceViewSet.as_view({'get': 'get_records'})(request).data
    return render(request, 'index.html', {'data': records})


class DeviceViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DeviceSerializer
    pagination_class = CustomPageNumber
    queryset = Device.objects.all().order_by('device_id')

    def get_records(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

    def list(self, request, *args):
        serializer = self.get_serializer(self.queryset, many=True)
        data = serializer.data
        return Response(data)
