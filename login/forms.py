from django import forms


class LoginForm(forms.Form):
	"""
		Form for user sign in.
		Fileds are: email address and password.
	"""
	email = forms.CharField(
		label="Adresse e-mail",
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
				'autocomplete': 'off'
			}
		)
	)
	password = forms.CharField(
		label="Mot de passe",
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control'
			}
		)
	)