from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()
    publish = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    image2 = models.ImageField(blank=True, upload_to='images/')
    image3 = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()
