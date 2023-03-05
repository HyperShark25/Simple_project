from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    title = models.CharField(max_length=20)
    serial_number = models.IntegerField(null=True)
    user = models.ForeignKey(User, help_text="The username attached to it", on_delete=models.CASCADE)
    date_created = models.DateTimeField(default="")
    binary = models.FloatField(null=True)

    def __str__(self):
        return self.title
