from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.publish.date() }'
