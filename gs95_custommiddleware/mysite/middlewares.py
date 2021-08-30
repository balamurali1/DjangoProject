#Process 1
"""
class UnderConstructionMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		print("Call From Middleware Before View")
		response = self.get_response(request) #idi view.py ni chupisthundi
		print("Call From Middleware After View")
		return response	
"""

#Process2
"""
from django.shortcuts import HttpResponse
class UnderConstructionMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		print("Call From Middleware Before View")
		response = HttpResponse("This is Under UnderConstruction")
		print("Call From Middleware After View")
		return response			
"""		


#Process3
from django.shortcuts import render
class UnderConstructionMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		print("Call From Middleware Before View")
		response = render(request,'mysite/siteuc.html')
		print("Call From Middleware After View")
		return response			