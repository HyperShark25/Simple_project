from .models import Device
from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
#    title = serializers.HyperlinkedRelatedField(view_name="Device", read_only=True, many=True)

    class Meta:
        model = Device
        fields = "__all__"
