from django import forms

class StudentRegistration(forms.Form):
	#name = forms.CharField(min_length = 5)
	#name = forms.CharField(max_length = 5)
	#name = forms.CharField(max_length = 50,strip = True)#by default (strip = True)strip ante value mundara space esthundi.
	#name = forms.CharField(empty_value = "Sonam")#(empty_value = required)
	#name = forms.CharField(error_messages = {'required':'Enter Your Name'}) #default ga Django ne error_message esthadi.danini change cheyali ante ela rayali.

    #short hand CharField
	name = forms.CharField(min_length = 5,max_length = 50,strip = False,
		empty_value = 'Sonam',error_messages = {'required':'Enter Your Name'})

	#IntegerField()
	roll = forms.IntegerField(min_value = 5,max_value = 40)

	#DecimalFiled()
	price = forms.DecimalField(min_value = 5,max_value = 40,max_digits = 4,decimal_places = 1)

	#FloatField()
	rate = forms.FloatField(min_value = 5,max_value = 40)

	#SlugField()
	comment = forms.SlugField()

	#EmailFiled()
	email = forms.EmailField(min_length = 5,max_length = 50)

	#URLField()
	website = forms.URLField(min_length = 5,max_length = 50)

	#CharFiled()
	password = forms.CharField(min_length = 5,max_length = 50,widget = forms.PasswordInput)

	description = forms.CharField(widget = forms.Textarea)

	feedback = forms.CharField(min_length = 5,max_length = 50,
		widget = forms.TextInput(attrs = {'class':'somecss1 somecss2',
			'id':'uniqueid'}))
	notes = forms.CharField(widget = forms.Textarea(attrs = {'row':3,'cols':50}))		 

	#BooleanField()
	#agree = forms.BooleanField()
	#agree = forms.BooleanField(label = 'I Agree')
	agree = forms.BooleanField(label_suffix = '',label = 'I Agree')
	#agree = forms.BooleanField(label_suffix = '',label = 'I Agree',error_messages = {'required':'Are You Agree'})










