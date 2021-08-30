from django.shortcuts import render

# Create your views here.

def fess_django(request):
    return render(request,'fees/feesone.html')

def fess_python(request):
    return render(request,'fees/feestwo.html')
