#Function Based Middleware
#Note: yeedi mundu print kavalo adi orderwise rasthamu.

def my_middleware(get_response):
	print("One Time Initialization")
	def my_function(request):
		print("This is  before view")
		response = get_response(request) #idi views lo unde danini print chesthundi.
		print('This is after view')
		return response
	return my_function		