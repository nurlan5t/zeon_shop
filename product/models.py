from django.core.exceptions import ValidationError
from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


def size_line_validator(size_line: str):
    """Validate size_line field in Product's objects."""
    first_two = size_line[:2]
    second_two = size_line[3:]
    if (first_two + second_two).isdigit()\
            and size_line[2] == '-' \
            and int(first_two) <= int(second_two)\
            and (int(first_two) + int(second_two)) % 2 == 0:
        return size_line
    raise ValidationError('Size must contain "-" between sizes(both evens) '
                          'and first size '
                          'less than second, example: 42-50')


class Collection(models.Model):
    """Collection model, represents Product's category."""

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return self.title


class Product(models.Model):
    """Product model, represents Product objects."""

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,
                                   related_name='collection')
    title = models.CharField(max_length=255)
    article = models.CharField(max_length=255, unique=True)
    actual_price = models.PositiveIntegerField(
        help_text="Актуальная цена на данный момент.")
    old_price = models.PositiveIntegerField(
        help_text="Цена до скидки, создаётся атвтоматически "
                  "после указания скидки.",
        default=None, null=True, blank=True
                                            )
    discount = models.PositiveIntegerField(
        help_text="Скидка в процентах.",
        default=None, null=True, blank=True)
    description = RichTextField()
    size_line = models.CharField(max_length=5,
                                 validators=(size_line_validator,))
    tissue_composition = models.CharField(max_length=250)
    quantity_in_line = models.PositiveIntegerField(
        help_text='Количество в линейке, создаётся атвтоматически '
                  'после линейки размеров.',
        blank=True)
    material = models.CharField(max_length=100)
    bestseller = models.BooleanField(default=False)
    novelty = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):

        """Define quantity_in_line."""
        first_two = self.size_line[:2]
        second_two = self.size_line[3:]
        self.quantity_in_line = (int(second_two) - int(first_two) + 2) // 2

        """Define an old_price if discount existing."""
        if self.discount is not None:
            self.old_price = self.actual_price
            self.actual_price = int(
                self.actual_price - (self.discount / 100 * self.actual_price)
            )
        super(Product, self).save(*args, **kwargs)


class ProductObjects(models.Model):
    """Relational model to Product, contains product's images and colors."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_objects')
    image = models.ImageField(upload_to='images/')
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = "Отдельный товар"
        verbose_name_plural = "Товары по отдельности"

    def __str__(self):
        return f"{self.product.title}   |   {self.color}    |   {self.image}"


class Cart(models.Model):
    """Cart contains all user chosen Products."""

    product = models.ForeignKey(ProductObjects, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f'{self.product.product.title} | {self.product.color}'


def calculate_order_info():
    """Calculate Cart objects and returns tuple of Order details."""
    lines_amount = Cart.objects.all().count()
    products_amount = sum(
        i.product.product.quantity_in_line *
        i.quantity for i in Cart.objects.all())
    total_price = sum(
        i.product.product.old_price * i.quantity for i in Cart.objects.all())
    actual_price = sum(
        i.product.product.actual_price * i.quantity for i in Cart.objects.all()
    )
    discount = total_price - actual_price
    return lines_amount, products_amount, total_price, actual_price, discount


ORDER_STATUSES = [
    ('НОВЫЙ', 'НОВЫЙ'),
    ('ОФОРМЛЕН', 'ОФОРМЛЕН'),
    ('ОТМЕНЕН', 'ОТМЕНЕН'),
]


class Order(models.Model):
    """Represents an Order objects."""

    '''Clients data.'''
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField(unique=False)
    country = CountryField()
    city = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUSES,
                              default=ORDER_STATUSES[0][1],
                              auto_created=True)
    public_agreement = models.BooleanField(default=False)
    ordered_products = models.ManyToManyField(Cart)

    '''Order sum calculate'''
    lines_amount = models.PositiveIntegerField(default=0)
    products_amount = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    actual_price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.lines_amount = calculate_order_info()[0]
        self.products_amount = calculate_order_info()[1]
        self.total_price = calculate_order_info()[2]
        self.actual_price = calculate_order_info()[3]
        self.discount = calculate_order_info()[4]
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.status
