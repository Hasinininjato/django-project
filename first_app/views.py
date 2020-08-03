from django.shortcuts import render

from first_app.forms import FirstAppForm


def index(request):
	if request.method == 'POST':
		form = FirstAppForm(request.POST)
		if form.is_valid():
			inputText = form.cleaned_data['inputText']
			envoi = True
	else:
		form = FirstAppForm()
	return render(request, 'first_app/first_app.html', locals())
