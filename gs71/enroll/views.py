from django.shortcuts import render
from . forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def regi(request):
	if request.method == 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			fm.save()
			#messages.add_message(request,messages.SUCCESS,'Your Account has been Created !!!')

									#(OR)
			messages.success(request,'Your Account has been Created !!!')						


			#messages.add_message(request,messages.INFO,'Now You can login !!!')
									#(OR)
			messages.info(request,'Now you can login !!!')						

	else:
		fm = StudentRegistration()

	return render(request,'enroll/userregistration.html',{'form':fm})			

