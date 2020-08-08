from django import forms


class LoginForm(forms.Form):
	"""
		User login form.
		Fields are: email address and password.
	"""
	email = forms.CharField(
		label=r"Email address",
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
				'autocomplete': 'off',
				'onkeyup': 'validationEmail("id_email", "Id_email")'
			}
		)
	)
	password = forms.CharField(
		label=r"Password",
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control'
			}
		)
	)
