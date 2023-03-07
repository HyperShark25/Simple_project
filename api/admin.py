from django.contrib import admin
from .models import Device


class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'serial_number', 'date_created']


admin.site.register(Device, DevicesAdmin)
