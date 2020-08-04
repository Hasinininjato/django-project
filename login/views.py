from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from login.forms import LoginForm


def connexion(request):
	error = False
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(username=email, password=password)
			if user:
				login(request, user)
			else:
				error = True
	else:
		form = LoginForm()
	return render(request, 'login/login.html', locals())
