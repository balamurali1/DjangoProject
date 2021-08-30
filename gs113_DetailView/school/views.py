from django.shortcuts import render
from . models import Student
from django.views.generic.detail import DetailView

# Create your views here.

class StudentDetailView(DetailView):
	model = Student
	

	# stud = Student.objects.all()
	# context = {'student':stud}
	# return render(request,'school/student_detail.html',context)	