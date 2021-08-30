from django.shortcuts import render
from django.views import View
from . forms import ContactForm
from django.http import HttpResponse

# Create your views here.

#Function Based Template's view
def homefun(request):
	return render(request,'school/home.html')


#Class Based Templates View
class HomeClassView(View):
	def get(self,request): #Idi Mandatory ga rayali.
		return render(request,'school/home.html')
###################################################

#Function Based Context view
def aboutfun(request):
	context = {'msg':'Welcome To GeekyShows Function Based View'}
	return render(request,'school/about.html',context)


#Class Based Context view
class AboutClassView(View):
	def get(self,request):
		context = {'msg':'Welcome To GeekyShows Class Based View'}
		return render(request,'school/about.html',context)

#########################################

#Function Based POST,GET 
def contactfun(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name'])
			return HttpResponse("Thank You Form Submitted!!")
	else:
		form = ContactForm()	 #ela rasthe empty form ani artham
	return render(request,'school/contact.html',{'form':form})			


#Class Based POST,GET
class ContactClassView(View):
	def get(self,request):
		form = ContactForm()  #ela rasthe empty form ani artham
		return render(request,'school/contact.html',{'form':form})

	def post(self,request):
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name'])
			return HttpResponse("Thank You Form Submitted!!")
##############################################
#Function Based View

# def newsfun(request):
# 	context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
# 	return render(request,'school/news.html',context)

# (or)

# def newsfun(request):
# 	template_name = 'school/news.html'
# 	context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
# 	return render(request,template_name,context)

#(or)

def newsfun(request,template_name):
	template_name = template_name
	context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
	return render(request,template_name,context)


#Class Based Views
# class NewClassView(View):
# 	def get(self,request):
# 		context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
# 		return render(request,'school/news.html',context)

#(or)

# class NewClassView(View):
# 	def get(self,request):
# 		template_name = 'school/news.html'
# 		context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
# 		return render(request,template_name,context)

#(or)

# class NewClassView(View):
# 	template_name = 'school/news.html'
# 	def get(self,request):
# 		context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
# 		return render(request,self.template_name,context)


#(or)

class NewClassView(View):
	template_name = ''
	def get(self,request):
		context = {'info':'CBI enquiry Why GeekyShows earns less Money'}
		return render(request,self.template_name,context)
##############################################