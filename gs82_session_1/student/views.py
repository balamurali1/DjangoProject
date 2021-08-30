from django.shortcuts import render

# Create your views here.

def setsession(request):
	request.session['name'] = 'Sonam'
	request.session['lname'] = 'Jha'
	return render(request,'student/setsession.html')


def getsession(request):
	name = request.session.get('name')
	keys = request.session.keys()   #key()
	items = request.session.items() #items()
	#age = request.session.setdefault('age','26')  #set()
	return render(request,'student/getsession.html',{'name':name,'keys':keys,
		'items':items})

def delsession(request):
	request.session.flush()  #flush() idi use chesthe total data remove auvthundi.
	return render(request,'student/delsession.html')
