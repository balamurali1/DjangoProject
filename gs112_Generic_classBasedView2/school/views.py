from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Student

# Create your views here.
class StudentListView(ListView):
	model = Student
	template_name = 'school/student.html'
	context_object_name = 'students'


	# stud = Student.objects.all()
	# context = {'student_list':stud}
	# return render(request,'school/student_list.html',context)