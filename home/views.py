from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='accounts/login')
def index(request):
	"""
		Only authenticated user can access the home page
		:param request:
		:return:
	"""
	return render(request, 'home/home.html', locals())
