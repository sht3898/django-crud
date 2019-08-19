from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 작성
    articles = Article.objects.order_by('-id')
    
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article.objects.create(title=title, content=content)
    article.save()
    context = {
        'article' : article
    }
    # return render(request, 'articles/create.html', context)
    return redirect('/articles/')

def delete(request):
    return render(request, 'articles/delete.html')