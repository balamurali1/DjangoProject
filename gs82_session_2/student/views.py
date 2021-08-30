from django.shortcuts import render

# Create your views here.

def setsession(request):
	request.session['name'] = 'Sonam'
	#request.session.set_expiry(600) #600 ante seconds ani artham.
			#(OR)
	#request.session.set_expiry(0) #0 ante seconds ani...
	request.session.set_expiry(10) #10 seconds ani
	return render(request,'student/setsession.html')


def getsession(request):
	name = request.session['name']
		#Print cheyadam,getsessionfile nundi,ela ikkadi nundi kuda print cheyavachunu. 
	print(request.session.get_session_cookie_age())
	print(request.session.get_expiry_age())
	print(request.session.get_expiry_date())
	print(request.session.get_expire_at_browser_close())
	return render(request,'student/getsession.html',{'name':name})

def delsession(request):
	request.session.flush()  #flush() idi use chesthe total data remove auvthundi.
	request.session.clear_expired()
	return render(request,'student/delsession.html')
