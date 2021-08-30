from django.shortcuts import render,HttpResponse
from . forms import ContactForm, FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.

class ContactFormView(FormView):
	template_name = 'school/contact.html'
	form_class  = ContactForm
	#form_class  = FeedbackForm
	success_url = '/thankyou/'
	initial = {'name':'Sonam'} #form lo fixed ga pettali ante ela

	def form_valid(self,form):
		print(form)
		print(form.cleaned_data['name'])
		print(form.cleaned_data['email'])
		print(form.cleaned_data['msg'])

		return super().form_valid(form)
		#return HttpResponse('Msg Sent')


class ThankTemplateView(TemplateView):
	template_name = 'school/thankyou.html'
