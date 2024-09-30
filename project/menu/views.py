from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Menu
from django.db import connection

def page_view(request, page_view):
    return render(request, 'index.html', {'item': page_view})

def index(request):
    return render(request, 'index.html')