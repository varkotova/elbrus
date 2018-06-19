import datetime
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Article(models.Model):
    article_date = models.DateField(verbose_name='Дата события')
    article_title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    article_image = models.ImageField(upload_to='upload_photo', blank=True, verbose_name='Фотография')
    article_description = models.TextField(blank=True, null=True, verbose_name='Описание статьи')
    article_text = models.TextField(blank=True, null=True, verbose_name='Текст статьи')

    def picture_micro_admin(self):
        if self.article_image:
            return format_html('<a href="' + self.article_image.url + '" target="_blank"><img src="' + self.article_image.url + '" width="100"/></a>')
        else:
            return '(Нет изображения)'
    picture_micro_admin.short_description = 'Миниатюра'
    picture_micro_admin.allow_tags = True

    def __str__(self):
        return '[{}] - {}'.format(self.article_date, self.article_title)




class Subscriber(models.Model):
    subscriber_name = models.CharField(max_length=100, blank=False, verbose_name='Имя подписчика')
    subscriber_email = models.EmailField(verbose_name='Email падписчика')
    subscriber_message = models.TextField(blank=False, verbose_name='Сообщение подписчика')
    subscriber_message_date = models.DateField(auto_now=True, verbose_name='Дата сообщения')

    def __str__(self):
        return '[{}] - {}'.format(self.subscriber_message_date, self.subscriber_name)
