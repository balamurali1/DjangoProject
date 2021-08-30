from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@method_decorator(login_required,name = 'dispatch') #ela single line lo  kuda rayavachunu
class ProfileTemplateView(TemplateView):
	template_name = 'registration/profile.html'

	

@method_decorator(staff_member_required, name = 'dispatch') #ela single  lo line kuda rayavachunu
class AboutTemplateView(TemplateView):
	template_name = 'registration/about.html'


	
