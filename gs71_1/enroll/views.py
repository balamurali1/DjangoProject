from django.shortcuts import render
from . forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def regi(request):
	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			fm.save()
			
			messages.info(request,'Now you can login !!!')
			print(messages.get_level(request))#already unna by default 'debug' value ni print chesha.idi cmd lo print auvthundi
			messages.debug(request,'This is Debu!!!')#idi kuda print kavali ante diniki 'set_level' create cheyali.
			messages.set_level(request,messages.DEBUG)#nenu debug value ni set chesha.idi cmd lo print auvthundi
			messages.debug(request,'This is New Debu!!!')
			print(messages.get_level(request))
			


	else:
		fm = StudentRegistration()

	return render(request,'enroll/userregistration.html',{'form':fm})			

