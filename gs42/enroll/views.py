from django.shortcuts import render
from . models import Student

# Create your views here.

def studentinfo(request):
	stud = Student.objects.all() #Student.object.all()=>sql Query set ni return chesthundi
	#stud = Student.objects.get(pk = 2)
	print("Myoutput", stud)
	return render(request,'enroll/studetails.html',{'stu':stud})