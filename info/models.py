from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


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


class SliderMainPage(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    link = models.URLField(blank=True, max_length=200)


class PublicOffer(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()


CALLED_CHOICES = [
    ('y', 'yes'),
    ('n', 'no'),
]


class CallBack(models.Model):
    user_name = models.CharField(max_length=250)
    user_phone = PhoneNumberField(null=False, unique=False)
    published = models.DateTimeField(auto_now_add=True)
    type_of_treatment = models.CharField(default='Callback', max_length=10)
    called_status = models.CharField(max_length=1, choices=CALLED_CHOICES,
                                     default='n')

