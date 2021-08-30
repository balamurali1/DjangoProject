from django.shortcuts import render
from django.core.cache import cache

# Create your views here.

	#get & set 
def home(request):
	mv = cache.get('movie','has_expired') #key,default(has_expired)
	if mv == 'has_expired':
		cache.set('movie','The Bahubali',30) #key,value,expired
		mv = cache.get('movie')
	return render(request,'enroll/course.html',{'fm':mv})


#get_or_set
# def home(request):
# 	mv = cache.get_or_set('fees',200,30,version=2)  #key,value,has_expired
# 	return render(request,'enroll/course.html',{'fm':mv})



#set_many & get_many
# def home(request):
# 	data = {'name':'Sonam','roll':101}
# 	cache.set_many(data,30)
# 	sv = cache.get_many(data)
# 	print(sv)
# 	return render(request,'enroll/course.html',{'stu':sv})

#delete
# def home(request):
# 	cache.delete('roll')
# 	return render(request,'enroll/course.html')

	#delete
# def home(request):
# 	cache.delete('fees',version = 2)
# 	return render(request,'enroll/course.html')


	#set & get
# def home(request):
# 	cache.set('roll',101,30)
# 	rv = cache.get('roll')
# 	print(rv)   #this line print in 'cmd' okay
# 	return render(request,'enroll/course.html')


	#decrement(decr)
# def home(request):
# 	dv = cache.decr('roll',delta = 1) #delta = 1 is the showing current value
# 	print(dv)
# 	return render(request,'enroll/course.html')

# def home(request):
# 	dv = cache.decr('roll',delta = 2) #delta = 2 is the decress the current value
# 	print(dv)
# 	return render(request,'enroll/course.html')	


#incress(incr)
# def home(request):
# 	dv = cache.incr('roll',delta = 3) #delta = 3 is the incress the current value
# 	print(dv)
# 	return render(request,'enroll/course.html')	

# def home(request):
# 	dv = cache.incr('roll',delta = 2) #delta = 2 is the incress the current value
# 	print(dv)
# 	return render(request,'enroll/course.html')

#clear()
# def home(request):
# 	cache.clear()
# 	return render(request,'enroll/course.html')