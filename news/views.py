from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news':news,
    }
    return render(request, 'news/index.html', context)

def detail(request, title):
    news = get_object_or_404(News, title=title)
    context = {
        'news':news,
    }
    return render(request, 'news/detail.html', context)