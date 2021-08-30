from django.shortcuts import render
from . models import Student

# Create your views here.
def home(request):
	#student_data = Student.objects.get(pk = 1)
	#(or)
	#student_data = Student.objects.get(id = 1)
	#student_data = Student.objects.get(name='Rohit')

	#student_data = Student.objects.first()
	#student_data = Student.objects.order_by('name').first()


	#student_data = Student.objects.last()
	#student_data = Student.objects.order_by('name').last()

	#student_data = Student.objects.latest('pass_date')
	
	#student_data = Student.objects.earliest('pass_date')


	#student_data = Student.objects.all()
	#print(student_data.exists())

	# student_data = Student.objects.all()
	# one_data = Student.objects.get(pk = 1)
	# print(student_data.filter(pk = one_data.pk).exists())


	#student_data = Student.objects.create(name = 'Sameer',roll = 114,
		#city = 'Bokaro',marks = 60,pass_date = '2020-5-4')


	# Note:table lo unde data nu tisukunte appudu get use auvthundi,new data nu rayali ante appudu create use auvthundi True vasthundi cmd lo	
	#student_data, created = Student.objects.get_or_create(name = 'Anisa',roll = 115,city = 'Bokaro',marks = 60,pass_date = '2020-5-4')	
	#print(created)  #idi cmd lo vasthundi create ayai nappudu True vasthundi.create kanappudud false vasthundi.

	#single record update
	#student_data = Student.objects.filter(id = 12).update(name = 'kabir',marks = 80)
	#Multiple records update
	#student_data = Student.objects.filter(marks = 70).update(city = 'Pass')

	
	# student_data,created = Student.objects.update_or_create(id = 14,name = 'Sameer',defaults = {'name':'kohli'})
	# print(created)


	#Note: ookokati kakunda ani okay sari create cheyadam.appudu 'bulk_create' use auvthundi.
	# objs = [
	# Student(name = 'Atif',roll = 116,city = 'Dhanbad',marks = 70,pass_date = '2020-5-4'),
	# Student(name = 'Sahil',roll = 117,city = 'Bokaro',marks = 50,pass_date = '2020-5-6'),
	# Student(name = 'kumar',roll = 118,city = 'Dhanbad',marks = 30,pass_date = '2020-5-9'),
	# ]
	# student_data = Student.objects.bulk_create(objs)


	# all_student_data = Student.objects.all()
	# for stu in all_student_data:
	# 	stu.city = "Dhanbad"
	# student_data = Student.objects.bulk_update(all_student_data,['city']) #['city']ante coloum name	


	# student_data = Student.objects.in_bulk([1,2]) #1,2 ante primarykey(pk),rows ani antaru
	# print(student_data[1].name)
	# print(student_data[2].marks)

	#Note: ikkada empty dictionary chupisthundi
	#student_data = Student.objects.in_bulk([])
	
	#Note:ikkada total records chupisthundi.
	#student_data = Student.objects.in_bulk()

	#single record delete
	#student_data = Student.objects.get(pk = 18).delete()

	#Multiple records delete
	#student_data = Student.objects.filter(marks = 50).delete()

	#Anni delete cheyali ante all().delete()
	#student_data = Student.objects.all().delete()

	#Table lo yenni records unnayaoo thelusukovachunu.ela
	student_data = Student.objects.all()
	print(student_data.count())










	print("Return:",student_data)
	return render(request,'school/home.html',{'student':student_data})