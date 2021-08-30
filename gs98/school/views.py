from django.shortcuts import render
from . models import Student
from datetime import date,time

# Create your views here.
def home(request):
	student_data = Student.objects.all()

	#student_data = Student.objects.filter(name__exact = "Sonam") #case-censitive
	#student_data = Student.objects.filter(name__iexact = "sonam") #case-incensitive

	#student_data = Student.objects.filter(name__contains = 'u') 
	#student_data = Student.objects.filter(name__icontains = 'U') 

	#NOte:manaku kavalasina records kosam ela filter cheyali
	#student_data = Student.objects.filter(id__in = [1,5,7]) 

	#NOte:60marks unna records ni filter cheyadam.
	#student_data = Student.objects.filter(marks__in = [60]) 
	#student_data = Student.objects.filter(marks__in = [60,70])

	#Note:graterthen 60 unna records ni filter cheyadam
	#student_data = Student.objects.filter(marks__gt =60) #graterthen

	#Note:graterthen equal 60 unna records ni filter cheyadam
	#student_data = Student.objects.filter(marks__gte =60)

	#Note:lessthen 60 unna records ni filter cheyadam.
	#student_data = Student.objects.filter(marks__lt =60)


	#Note:lessthen equal 60 unna records ni filter cheyadam.
	#student_data = Student.objects.filter(marks__lte =60)

	#student_data = Student.objects.filter(name__startswith = 's')
	#student_data = Student.objects.filter(name__istartswith = 'S')

	#student_data = Student.objects.filter(name__endswith = 'l')
	#student_data = Student.objects.filter(name__iendswith = 'L')

	#Note:format(yyyy-mm-dd)
	#student_data = Student.objects.filter(passdate__range = ('2020-04-01','2020-05-03'))

	#Note:specific date record's kavali ante ela
	#student_data = Student.objects.filter(admdatetime__date = date(2020,1,3))
	#student_data = Student.objects.filter(admdatetime__date = date(2020,2,5))

	#student_data = Student.objects.filter(admdatetime__date__gt = date(2020,1,4))
	#student_data = Student.objects.filter(admdatetime__date__gte = date(2020,1,4))

	#student_data = Student.objects.filter(admdatetime__date__lt = date(2020,1,4))
	#student_data = Student.objects.filter(admdatetime__date__lte = date(2020,1,10))


	#student_data = Student.objects.filter(passdate__year = 2020)
	#student_data = Student.objects.filter(passdate__year = 2019)
	#student_data = Student.objects.filter(passdate__year__gt = 2019)
	#student_data = Student.objects.filter(passdate__year__gte = 2019)


	#student_data = Student.objects.filter(passdate__month = 4)
	#student_data = Student.objects.filter(passdate__month = 5)
	#student_data = Student.objects.filter(passdate__month__gt = 4)
	#student_data = Student.objects.filter(passdate__month__gte = 4)


	#student_data = Student.objects.filter(passdate__day= 2)
	#student_data = Student.objects.filter(passdate__day__gt= 2)
	#student_data = Student.objects.filter(passdate__day__gte= 2)	

	#14weeks sambandinchina data kavali ante ela..
	#student_data = Student.objects.filter(passdate__week= 14)
	#student_data = Student.objects.filter(passdate__week__gt= 14)

	#Note:sun = 1,mon= 2,Tue = 3,Wed = 4,Thu = 5,Fri = 6,sta = 7
	#student_data = Student.objects.filter(passdate__week_day= 5)
	#student_data = Student.objects.filter(passdate__week_day__gt= 5)

	#Note:Jan to Mar(1 quarter),Apr to Jun(2 quarter),july to sep(3 quarter),Oct to Dem(4 quarter)
	#student_data = Student.objects.filter(passdate__quarter = 2)

	#student_data = Student.objects.filter(admdatetime__time__gt = time(6,00))
	#student_data = Student.objects.filter(admdatetime__time__gt = time(21,17))

	#Note:hour's(0 to 23)
	#student_data = Student.objects.filter(admdatetime__hour = 6)
	#student_data = Student.objects.filter(admdatetime__hour__gt = 6)

	#NOte: minute(0 to 59)
	#student_data = Student.objects.filter(admdatetime__minute =25 )
	#student_data = Student.objects.filter(admdatetime__minute__gt =26 )
	#student_data = Student.objects.filter(admdatetime__minute__gt =20 )

	#Second's
	#student_data = Student.objects.filter(admdatetime__second__gt =20 )
	#student_data = Student.objects.filter(admdatetime__second =20 )

	#isnull
	#student_data = Student.objects.filter(roll__isnull = True )
	#student_data = Student.objects.filter(roll__isnull = False )




	print("Return:",student_data)
	print()
	print('SQL Query:',student_data.query)
	return render(request,'school/home.html',{'students':student_data})
