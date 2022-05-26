from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "News"


class AboutUs(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    image2 = models.ImageField(blank=True, upload_to='images/')
    image3 = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class HelpQA(models.Model):
    question = models.CharField(max_length=250)
    answer = RichTextField()
    image = models.ImageField(blank=True, upload_to='images/')

    class Meta:
        verbose_name = "Q&A"
        verbose_name_plural = "Help Q&A"


class OurAdvantages(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        verbose_name = "Advantage"
        verbose_name_plural = "Our Advantages"

    def __str__(self):
        return f'{self.title}'
