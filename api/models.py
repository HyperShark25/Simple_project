from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Device(models.Model):
    title = models.CharField(max_length=20)
    serial_number = models.IntegerField(null=True)
    user = models.ForeignKey(User, help_text="The username attached to it", on_delete=models.CASCADE)
    date_created = models.DateTimeField(default="")

# def get_absolute_url(self):
#     """Returns the URL to access a particular instance of the model."""
#     return reverse('dragon')


#     return reverse('model-detail-view', args=[str(self.id)])
# Note: Assuming you will use URLs like /myapplication/mymodelname/2 to display individual records for your
# model (where "2" is the id for a particular record), you will need to create a URL mapper to pass the
# response and id to a "model detail view" (which will do the work required to display the record). The reverse
# () function above is able to "reverse" your URL mapper (in the above case named 'model-detail-view') in order
# to create a URL of the right format.

# Of course to make this work you still have to write the URL mapping, view, and template!

# You can also define any other methods you like, and call them from your code or templates (provided that they
# don't take any parameters).

    def __str__(self):
        return self.title
