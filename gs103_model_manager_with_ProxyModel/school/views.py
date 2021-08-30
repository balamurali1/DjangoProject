from django.shortcuts import render
from . models import Student,ProxyStudent

# Create your views here.
def home(request):
	student_data = Student.objects.all() #"objects" is model manager,this is by default
	#student_data = ProxyStudent.students.all()
	#student_data = ProxyStudent.students.get_stu_roll_range(103,109) #"students" is model manager ,this is i am created manuvally
	return render(request,'school/home.html',{'students':student_data})