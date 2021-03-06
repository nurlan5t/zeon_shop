# Generated by Django 4.0.4 on 2022-06-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_footerheaderobjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageHelpQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Картинка "помощи"',
                'verbose_name_plural': 'Картинка "помощи"',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='callback',
            options={'verbose_name': 'Обратный звонок', 'verbose_name_plural': 'Обратные звонки'},
        ),
        migrations.AlterModelOptions(
            name='footerheaderobjects',
            options={'verbose_name': 'Объект Хедера и Футера', 'verbose_name_plural': 'Объекты Хедера и Футера'},
        ),
        migrations.AlterModelOptions(
            name='helpqa',
            options={'verbose_name': 'Помощь Вопрос-Ответ', 'verbose_name_plural': 'Помощь Вопросы-Ответы'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='ouradvantages',
            options={'verbose_name': 'Наше преимущество', 'verbose_name_plural': 'Наши преимущества'},
        ),
        migrations.AlterModelOptions(
            name='publicoffer',
            options={'verbose_name': 'Публичная оферта', 'verbose_name_plural': 'Публичная оферта'},
        ),
        migrations.AlterModelOptions(
            name='slidermainpage',
            options={'verbose_name': 'Слайдер (Главная страница)', 'verbose_name_plural': 'Слайдер (Главная страница)'},
        ),
        migrations.AlterModelOptions(
            name='socialtypes',
            options={'verbose_name': 'Тип связи', 'verbose_name_plural': 'Типы звязи'},
        ),
        migrations.RemoveField(
            model_name='helpqa',
            name='image',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image2',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image3',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='callback',
            name='type_of_treatment',
            field=models.CharField(default='Обратный звонок', max_length=10),
        ),
        migrations.AlterField(
            model_name='footerheaderobjects',
            name='footer_logo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='footerheaderobjects',
            name='header_logo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='footerheaderobjects',
            name='text_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ouradvantages',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='slidermainpage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='slidermainpage',
            name='link',
            field=models.URLField(),
        ),
    ]
