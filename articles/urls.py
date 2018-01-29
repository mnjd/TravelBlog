"""travelblog URL Configuration

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
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^detail/(?P<pk>\d+)$', views.article_detail, name='article_detail'),
    url(r'^create/', views.create_article, name='create_article'),
    url(r'^edit/(?P<pk>\d+)$', views.edit_article, name='edit_article'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_article, name='delete_article')
]
