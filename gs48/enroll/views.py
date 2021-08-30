from django.shortcuts import render	
from . forms import StudentRegistration 

# Create your views here.

def showformdata(request):
	fm = StudentRegistration(auto_id = True,label_suffix = '-',
		initial = {'name':'Bala Murali','email':'sonam@gmail.com'})

	#fm.order_fields(field_order = None) #None is default
	#fm.order_fields(field_order = ['email','name','first_name'])
	fm.order_fields(field_order = ['email','first_name','name'])
	
	return render(request,'enroll/userregistration.html',{'form':fm})
