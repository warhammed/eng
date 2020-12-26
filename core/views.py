from django.shortcuts import render
from news.models import News

def index(request):
    news = News.objects.all()[:3]
    context={
        'news':news,
    }
    return render(request, 'index.html', context)

def introducing(request):
    return render(request, 'pages/introducing.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})

def managers(request):
    return render(request, 'pages/managers.html', {})

def labs(request):
    return render(request, 'pages/labs.html', {})

def error404(request, exception):
    return render(request, 'pages/error404.html', context={}, status=404)
    
def error500(request):
    return render(request, 'pages/error500.html', context={})