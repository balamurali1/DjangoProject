from django.shortcuts import render
from . models import Student,Teacher
from django.db.models import Q

# Create your views here.
def home(request):
	student_data = Student.objects.all()   #fields ante coloumns names ani artham.

	#student_data  = Student.objects.filter(marks = 70) #marks(column name),70(value))

	#student_data  = Student.objects.exclude(marks = 70) #dinini vadilesi megathavi chupinchu.

	#student_data  = Student.objects.order_by('city') #order ga chupinchu ani artham
	#student_data  = Student.objects.order_by('marks') #Ascending(Asc) order lo vasthai
	#student_data  = Student.objects.order_by('-marks') #Decending Order lo vasthai
	#student_data  = Student.objects.order_by('?') #jambling auvthu untai..
	#student_data  = Student.objects.order_by('name') #(Asc)name's anni alphabetical order lo vastai.
	#student_data  = Student.objects.order_by('-name')


	#student_data  = Student.objects.order_by('id')
	#student_data  = Student.objects.order_by('id').reverse()
	#student_data  = Student.objects.order_by('id').reverse()[:5]  #[:5] ante python lo slicing use cheshanu.


	#student_data  = Student.objects.values()
	#student_data  = Student.objects.values('name','city') #specific columns kavali ante ela


	#student_data  = Student.objects.values_list() #cmd lo chupisthundi
	#student_data  = Student.objects.values_list('id','name') #cmd lo chupistundi
	#student_data  = Student.objects.values_list('id','name',named = True) #by defalut ga false untadi chudu.Specific columns kavali ante ela


	#student_data  = Student.objects.using('default')


	#student_data  = Student.objects.dates('pass_date','month') #pass_date column  lo yenni month's include aayai nayoo telusukovachunu
	#student_data  = Student.objects.dates('pass_date','year')


	#student_data  = Student.objects.none()

###########Second Tables 'Teacher' Started ########
	#qs1 = Student.objects.values_list('id','name',named = True)
	#qs2 = Teacher.objects.values_list('id','name',named = True)
	#student_data = qs2.union(qs1) #union anedi combined(duplicate ni elemenet chesi anitini kaluputhundi okay table lo) chesthundi
 

	# qs1 = Student.objects.values_list('id','name',named = True)
	# qs2 = Teacher.objects.values_list('id','name',named = True)
	# student_data = qs2.union(qs1,all = True)


	#Note:id same undi ,name same unte ikkada chupisthundi.
	# qs1 = Student.objects.values_list('id','name',named = True)
	# qs2 = Teacher.objects.values_list('id','name',named = True)
	# student_data = qs2.intersection(qs1)

	# qs1 = Student.objects.values_list('id','name',named = True)
	# qs2 = Teacher.objects.values_list('id','name',named = True)
	# student_data = qs1.intersection(qs2)


	#Note: id same undakunda, name same undakunda unte ikkada chupisthundi.
	# qs1 = Student.objects.values_list('id','name',named = True)
	# qs2 = Teacher.objects.values_list('id','name',named = True)
	# student_data = qs1.difference(qs2)  #qs1 - qs2


	# qs1 = Student.objects.values_list('id','name',named = True)
	# qs2 = Teacher.objects.values_list('id','name',named = True)
	# student_data = qs2.difference(qs1)  #qs2 - qs1

################# AND  OR  Operator ##########

	#student_data = Student.objects.filter(id = 6) & Student.objects.filter(roll = 106)
	#student_data = Student.objects.filter(id = 7) & Student.objects.filter(name = 'Ali')
	# (or)
	#student_data = Student.objects.filter(id = 6,roll = 106)
	#(or)
	#student_data = Student.objects.filter(Q(id = 6) & Q(roll = 106))



	#student_data = Student.objects.filter(id = 6) | Student.objects.filter(roll = 106)
	#student_data = Student.objects.filter(id = 6) | Student.objects.filter(roll = 107)
	#student_data = Student.objects.filter(Q(id = 6) | Q(roll = 106))
	#student_data = Student.objects.filter(Q(id = 6) | Q(roll = 108))



	print("Return:",student_data) #ela rasthe cmd lo chudavachunu
	print()
	print("SQL Query:",student_data.query)
	return render(request,'school/home.html',{'students':student_data})