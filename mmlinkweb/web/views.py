from django.shortcuts import render, redirect
from .models import*
from .form import*
from django.utils.translation import gettext as _
from django.contrib import messages
# Create your views here.



def index(request):
	trans = _('hello')
	return render (request, 'web/home.html', {'trans': trans})



def about(request):
	return render (request, 'web/about.html')


def plan(request):
	return render (request, 'web/plan.html')



def feature(request):
	return render (request, 'web/feature.html')



def form(request):
	return render (request, 'web/form.html')


def complain(request):
	form = ComplainForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Your complain has been send!!!!')
	form = ComplainForm()
	complains = Complain.objects.all()
	context = {'complain': complains, 'form':form}
	return render (request, 'web/complain.html', context)


def newinstallation(request):
	form = NewInstallationForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Your Installation Form  have successful!!!!')
	form = NewInstallationForm()
	complains = NewInstallation.objects.all()
	context = {'newinstallation': newinstallation, 'form':form}
	return render (request, 'web/newinstallation.html', context)




def billing(request):
	if request.method == "POST":
		form = BillingForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		messages.success(request, 'Your bill has been send!!!!')
		
	form = BillingForm()
	bill = Billing.objects.all()
	context = {'bill':billing, 'form':form}
	return render (request, 'web/billing.html', context)




def contact(request):
	return render (request, 'web/contact.html')