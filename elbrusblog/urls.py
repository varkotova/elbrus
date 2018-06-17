"""elbrusblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from elbrusblog import views


urlpatterns = [
    path('', views.index, name=''),
    path('index', views.index, name='index'),
    path('page/<int:num_page>', views.articles_page, name='articles_page'),
    path('page/<int:num_page>/<int:num_article>', views.article_page, name='article_page'),



    path('generic', views.generic, name='generic'),
    path('elements', views.elements, name='elements'),


]
