from django.shortcuts import render
from .models import Staff
from django.core.paginator import Paginator

def index(request):
    staff_list = Staff.objects.all()
    staff_count = staff_list.count()
    paginator = Paginator(staff_list, 10)
    page_number = request.GET.get('page')
    staff = paginator.get_page(page_number)
    context ={
        'staff':staff,
        'staff_count':staff_count,
    }
    return render(request, 'staff/index.html', context)