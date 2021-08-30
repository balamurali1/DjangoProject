from django.shortcuts import render
from . models import Student
from django.db.models import Q

# Create your views here.
def home(request):
	#student_data = Student.objects.filter(Q(id = 6) & Q(roll = 106))

	#student_data = Student.objects.filter(Q(id = 6) & Q(roll = 107)) #output radu.id and roll same row lo undali

	#student_data = Student.objects.filter(Q(id = 6) | Q(roll = 106))
	#student_data = Student.objects.filter(Q(id = 6) | Q(roll = 107))

	#Note:id 6 row okati radu migathavi vasthai
	#student_data = Student.objects.filter(~Q(id = 6))

	#Note:id 8 row okati radu migathavi vasthai
	student_data = Student.objects.filter(~Q(id = 8))




	print("Return:",student_data)
	print()
	print('SQL Query:',student_data.query)
	return render(request,'school/home.html',{'students':student_data})
