from django.shortcuts import render


# Create your views here.

def learn_django(request):
    cname = 'Django'	#This is Dynamic code(pythoncode)(7 to 10)
    duration = '4 Months'
    seats = 10
    django_details = {'nm':cname,'du':duration,'st':seats}
    return render(request,'course/courseone.html',django_details)

def learn_python(request):
    return render(request,'course/coursetwo.html')
