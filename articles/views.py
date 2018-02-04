from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, CreateView, DeleteView
from django.utils import timezone
from .models import Articles
from .forms import ArticlesForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def blog(request):
    blog = Articles.objects.all().order_by('-created_at')
    context = {'articles': blog}
    return render(request, 'articles/ListArticles.html', context)

def article_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/DetailArticle.html', context)

@login_required(login_url="/users/login/")
def create_article(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.author = request.user
            newform.save()
        return redirect('articles:blog')
    else:
        form = ArticlesForm()       
    return render(request, 'articles/CreateArticle.html', { 'form':form })

'''
def create_article(request):
    if request.POST == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.save()
        return redirect('articles:blog')
    else:
        form = ArticlesForm()
    return render(request, 'articles/CreateArticle.html', {'form':form})
'''

@login_required(login_url="/users/login/")
def edit_article(request, pk=None):
    article = get_object_or_404(Articles, pk=pk)
    form = ArticlesForm(request.POST or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.updated_at = timezone.now()
        article.save()
        return redirect('articles:blog')

    context = {'title':article.title, 'article':article, 'form':form}
    return render(request, 'articles/EditArticle.html', context)

@login_required(login_url="/users/login/")
def delete_article(request, pk=None):
    article = get_object_or_404(Articles, pk=pk)
    article.delete()
    return redirect('articles:blog')


