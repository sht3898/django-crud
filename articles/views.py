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
    return redirect(f'/articles/{article.pk}/')

def detail(request, article_pk):
    # article_pk를 인자로 따로 만들어줘야 함
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request):
    num = request.GET.get('num')
    print(num)
    article = Article.objects.get(pk=num)
    context = {
        'num' : num
    }
    article.delete()
    return render(request, 'articles/delete.html', context)

def one(request):
    return render(request, 'articles/one.html')

def two(request):
    return render(request, 'articles/two.html')