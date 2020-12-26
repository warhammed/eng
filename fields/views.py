from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Degree, Field

def index(request):
    degrees = Degree.objects.all()
    context = {
        'degrees':degrees,
    }
    return render(request, 'fields/index.html', context)

def degree_detail(request, degree_slug):
    degree = Degree.objects.get(slug=degree_slug)
    context = {
        'degree':degree,
    }
    return render(request, 'fields/degree_detail.html', context)

def field_detail(request, degree_slug, field_slug):
    if field_slug.endswith('/'):
        field_slug=field_slug[:-1]
    degree = get_object_or_404(Degree, slug=degree_slug)
    field = get_object_or_404(Field, degree=degree, slug=field_slug)
    context = {
        'degree':degree,
        'field':field,
    }
    return render(request, 'fields/field_detail.html', context)