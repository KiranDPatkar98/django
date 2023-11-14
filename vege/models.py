from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Reciepe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')

    # Add a default manager
    objects = models.Manager()
