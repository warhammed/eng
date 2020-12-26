from django.shortcuts import render, get_object_or_404
from .models import Group

def index(request):
    groups = Group.objects.all()
    context = {
        'groups':groups,
    }
    return render(request, 'groups/index.html', context)

def group_detail(request, slug):
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group':group,
    }
    return render(request, 'groups/detail.html', context)