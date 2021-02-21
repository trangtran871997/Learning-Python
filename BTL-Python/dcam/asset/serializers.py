from rest_framework import serializers
from asset.models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    license = serializers.SlugRelatedField(many=True, read_only=True, slug_field='end_time')
    management = serializers.SlugRelatedField(many=True, read_only=True, slug_field='owner')

    class Meta:
        model = Device
        fields = ['device_id', 'name', 'description', 'quantity', 'status', 'note', 'license', 'management']
