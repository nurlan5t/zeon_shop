from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class News(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class AboutUs(models.Model):
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class ImageHelpQA(models.Model):
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Картинка \"помощи\""
        verbose_name_plural = "Картинка \"помощи\""


class HelpQA(models.Model):
    question = models.CharField(max_length=250)
    answer = RichTextField()

    class Meta:
        verbose_name = "Помощь Вопрос-Ответ"
        verbose_name_plural = "Помощь Вопросы-Ответы"


class OurAdvantages(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        verbose_name = "Наше преимущество"
        verbose_name_plural = "Наши преимущества"

    def __str__(self):
        return f'{self.title}'


class SliderMainPage(models.Model):
    image = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name = "Слайдер (Главная страница)"
        verbose_name_plural = "Слайдер (Главная страница)"


class PublicOffer(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()

    class Meta:
        verbose_name = "Публичная оферта"
        verbose_name_plural = "Публичная оферта"


CALLED_CHOICES = [
    ('y', 'yes'),
    ('n', 'no'),
]


class CallBack(models.Model):
    user_name = models.CharField(max_length=250)
    user_phone = PhoneNumberField(unique=False)
    published = models.DateTimeField(auto_now_add=True)
    type_of_treatment = models.CharField(default='Обратный звонок',
                                         max_length=10)
    called_status = models.CharField(max_length=1, choices=CALLED_CHOICES,
                                     default='n')

    class Meta:
        verbose_name = "Обратный звонок"
        verbose_name_plural = "Обратные звонки"


CONTACT_TYPES = [
    ('PHONE', 'PHONE'),
    ('WHATSAPP', 'WHATSAPP'),
    ('INSTAGRAM', 'INSTAGRAM'),
    ('TELEGRAM', 'TELEGRAM'),
    ('EMAIL', 'EMAIL'),
]


class SocialTypes(models.Model):
    contact_type = models.CharField(
        max_length=100, help_text='Choose from list', choices=CONTACT_TYPES)
    link_to = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Тип связи"
        verbose_name_plural = "Типы звязи"

    def save(self, *args, **kwargs):
        """Возвращает ссылку на Whatsapp, если тип связи WHATSAPP."""
        if self.contact_type == 'WHATSAPP':
            # Исключает первую строку номера ('+')
            self.link_to = 'https://wa.me/' + str(self.link_to[1:])
        super(SocialTypes, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.contact_type},   {self.link_to}'


class FooterHeaderObjects(models.Model):
    header_logo = models.ImageField(upload_to='images/')
    footer_logo = models.ImageField(upload_to='images/')
    text_info = models.TextField()
    header_phone = PhoneNumberField(unique=False)
    social_type = models.ManyToManyField(SocialTypes)

    class Meta:
        verbose_name = "Объект Хедера и Футера"
        verbose_name_plural = "Объекты Хедера и Футера"
