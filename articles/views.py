from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, DeleteView
from .models import Articles
from .forms import ArticlesForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

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
        return HttpResponseRedirect('articles/blog.html')
        
    context = {'form':form}        
    return render(request, 'articles/CreateArticle.html', context)
