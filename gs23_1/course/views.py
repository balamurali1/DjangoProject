from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('Hello Python')
