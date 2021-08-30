from django.shortcuts import render,HttpResponse

# Create your views here.

def setsession(request):
	request.session['name'] = 'Sonam' 
	return render(request,'student/setsession.html')


def getsession(request):
	if 'name' in request.session:
		request.session.modified = True
		name = request.session['name']
		return render(request,'student/getsession.html',{'name':name})
	else:
		return HttpResponse("Your Session has Expired....")	

def delsession(request):
	request.session.flush()  #flush() idi use chesthe total data remove auvthundi.
	request.session.clear_expired()
	return render(request,'student/delsession.html')
