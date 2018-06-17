from django.shortcuts import render

from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'elbrusblog/index.html', context)






def articles_page(request, num_page):
    articles = Article.objects.all().order_by('article_title')
    context = {
        'articles': articles,
    }

    return render(request, 'elbrusblog/articles_page.html', context)



def article_page(request, num_article):


    return render(request, 'elbrusblog/article.html')








def generic(request):
    return render(request, 'elbrusblog/generic.html')


def elements(request):
    return render(request, 'elbrusblog/elements.html')