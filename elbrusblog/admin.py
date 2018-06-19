from django.contrib import admin
from .models import Article, Subscriber


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_date', 'article_title', 'article_description', 'picture_micro_admin']
    # list_display = [field.name for field in Article._meta.fields]
    readonly_fields = ['picture_micro_admin',]

    # только по одному полю:
    # list_filter = ['article_title',]

    # list_filter = ['article_title', 'article_date']
    # search_fields = ['article_title', 'article_date']

    # убрать или оставить только те поля, которые нужны на странице article в БД
    # exclude = ['article_text']
    # fields = ['article_date', 'article_title', 'article_image', 'picture_micro_admin']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
