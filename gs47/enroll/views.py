from django.shortcuts import render
from . forms import StudentRegistration

# Create your views here.

def showformdata(request):
	#fm = StudentRegistration(auto_id ="geeky") #"geeky" = True,fm = object antaru
	fm = StudentRegistration(auto_id =True,label_suffix = ' -',
	initial = {'name':'Murali','email':'sonam@geekyshows.com'})  #auto_id = True(default)
	#fm = StudentRegistration(auto_id =False)
	#fm = StudentRegistration(auto_id ='some_%s') #%s = field names chupistundi
	return render(request,'enroll/userregistration.html',{'form':fm})
 