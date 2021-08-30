from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

#Function Based View
def myview(request):
	return HttpResponse("<h1>This is Function Based View</h1>")


#class Based view
class MyView(View):
	name = "Sonam"  #Attributes
	#name = ''      #'' empty ga  petti url lo name ='Rahul' rasina....
	def get(self,request):		
		#return HttpResponse("<h1>This is Class Based View-GET</h1>")
		return HttpResponse(self.name)

class MyViewChild(MyView):
	def get(self,request):
		return HttpResponse(self.name)		