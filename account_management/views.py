from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from account_management.forms.login.forms import LoginForm


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
