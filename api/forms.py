from .models import Device
from django import forms


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

