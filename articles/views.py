from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, CreateView, DeleteView
from .models import Articles
from .forms import ArticlesForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def blog(request):
    blog = Articles.objects.all().order_by('-created_at')
    context = {'articles': blog}
    return render(request, 'articles/ListArticles.html', context)

def article_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/DetailArticle.html', context)

def create_article(request):
    form = ArticlesForm(request.POST)
    if form.is_valid():
        newform = form.save(commit=False)
        newform.save()
        return HttpResponseRedirect(reverse('articles:blog'))
        
    context = {'form':form}        
    return render(request, 'articles/CreateArticle.html', context)

def edit_article(request, pk=None):
    article = get_object_or_404(Articles, pk=pk)
    form = ArticlesForm(request.POST or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
        return HttpResponseRedirect(reverse('articles:blog'))

    context = {'title':article.title, 'article':article, 'form':form}
    return render(request, 'articles/EditArticle.html', context)

def delete_article(request, pk=None):
    article = get_object_or_404(Articles, pk=pk)
    article.delete()
    return HttpResponseRedirect(reverse('articles:blog'))


