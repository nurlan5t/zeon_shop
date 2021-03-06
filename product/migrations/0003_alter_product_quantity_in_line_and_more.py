# Generated by Django 4.0.4 on 2022-06-02 12:53

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_productobjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_in_line',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_line',
            field=models.CharField(max_length=5, validators=[product.models.size_line_validator]),
        ),
    ]
