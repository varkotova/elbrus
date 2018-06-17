# Generated by Django 2.0.1 on 2018-04-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elbrusblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='upload_photo', verbose_name='Фотография'),
        ),
    ]