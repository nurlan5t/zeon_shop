from django.db import models


class Collection(models.Model):
    """Collection model, represents Product's category."""

    image = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
