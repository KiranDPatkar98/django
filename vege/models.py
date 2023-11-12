from django.db import models

# Create your models here.


class Reciepe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')

    # Add a default manager
    objects = models.Manager()
