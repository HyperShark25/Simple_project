from django.contrib import admin
from .models import Device, New


class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'serial_number', 'date_created']


class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'secret_number', 'duration']


admin.site.register(Device, DevicesAdmin)
admin.site.register(New, NewAdmin)
