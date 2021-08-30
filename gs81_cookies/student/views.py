from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.

def setcookie(request):
	reponse =  render(request,'student/setcookie.html')
	#reponse.set_cookie('name','sonam',max_age = 60)	#60 ate seconds ani arthamvasthundi
	#reponse.set_cookie('name','sonam',expires = datetime.utcnow()+timedelta(days = 2))
			#set the value
	#reponse.set_cookie('name','Rahul',expires = datetime.utcnow()+timedelta(days = 2))
			#set the key and value
	reponse.set_cookie('lname','Jha',expires = datetime.utcnow()+timedelta(days = 2))		
	return reponse



def getcookie(request):
	#name = request.COOKIES['name']
		#(OR)
	name = request.COOKIES.get('name')
	name = request.COOKIES.get('name','Guest')
	return render (request,'student/getcookie.html', {'name':name})


def delcookie(request):
	reponse = render(request,'student/delcookie.html')
	reponse.delete_cookie('name')
	return reponse
