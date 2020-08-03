from django import forms


class FirstAppForm(forms.Form):
	inputText = forms.CharField(label="Your text here", max_length=100)
