# from django import forms
from django.forms import ModelForm
from .models import*

class ComplainForm(ModelForm):
	class Meta:
		model = Complain
		fields = ('name', 'customer_id', 'router', 'phone_number','address', 'comment')
		



class NewInstallationForm(ModelForm):
	class Meta:
		model = NewInstallation
		fields = "__all__"



class BillingForm(ModelForm):
	class Meta:
		model = Billing
		fields = ('name', 'customer_id', 'bill_screenshot', 'remark')
