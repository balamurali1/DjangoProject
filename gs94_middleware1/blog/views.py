from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
	print("I am views")
	print("Hello")
	return HttpResponse("This is Home Page")