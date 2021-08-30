from django import forms
from . models import User

 
class StudentRegistration(forms.ModelForm):
#ela change cheyadanekey ee floder create cheshadu. EX:name,email,password
#ee file lo 'name'filed type attributes change cheyadam.alrady models.py lo undi kani ikkada change cheyadam.
	name = forms.CharField(max_length = 50,required = False)#required = False idid error ki sambandinchinadi.
	
	class Meta:
		model = User
		fields = ['name','email','password'] 
		labels = {'name' : 'Enter Name','email':'Enter Email','password':'Enter Password'}	 
		widgets = {'password':forms.PasswordInput}
		