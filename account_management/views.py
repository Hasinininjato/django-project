from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from account_management.forms.login.forms import LoginForm
from account_management.forms.register.forms import RegisterForm
from account_management.models import CustomUser


def app_login(request):
	error = False
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(request, email=email, password=password)
			if user:
				login(request, user)
				return HttpResponseRedirect('/', locals())
			else:
				error = True
	else:
		form = LoginForm()
	return render(request, 'account_management/login/login.html', locals())


def app_logout(request):
	logout(request)
	return redirect(reverse(app_login))


def app_register(request):
	error = False
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			
			user_email = CustomUser.objects.filter(email=email)
			if user_email is not None:
				return HttpResponseRedirect('register', locals())
			
			user = CustomUser.objects.create_user(
				email=email,
				password=password,
				first_name=first_name,
				last_name=last_name
			)
			return HttpResponseRedirect('/', locals())
	else:
		form = RegisterForm()
	return render(request, 'account_management/register/register.html', locals())
