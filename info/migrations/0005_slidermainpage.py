# Generated by Django 4.0.4 on 2022-05-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_ouradvantages_alter_aboutus_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]