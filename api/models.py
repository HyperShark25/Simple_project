from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Device(models.Model):
    title = models.CharField(max_length=20)
    serial_number = models.IntegerField(null=True)
    user = models.ForeignKey(User, help_text="The username attached to it", on_delete=models.CASCADE)
    date_created = models.DateTimeField(default="")

    def __str__(self):
        return self.title


class New(models.Model):
    secret_number = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], null=True)
    duration = models.DurationField(null=True)
