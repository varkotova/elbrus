# Generated by Django 2.0.1 on 2018-06-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elbrusblog', '0004_auto_20180607_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_name', models.CharField(max_length=100)),
                ('subscriber_email', models.EmailField(max_length=254)),
                ('subscriber_message', models.TextField()),
                ('subscriber_message_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
