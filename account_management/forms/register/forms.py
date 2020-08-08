from django import forms


class RegisterForm(forms.Form):
	"""
		User register form.
		Fields are:
			first_name
			last_name
			email
			password
		To extend the model, add some extra fields in the model CustomUser.
	"""
	first_name = forms.CharField(
		label=r"First name",
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'autocomplete': 'off',
				'onkeyup': 'validationField("id_first_name", "Id_first_name")'
			}
		)
	)
	last_name = forms.CharField(
		label=r"Last name",
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'autocomplete': 'off',
				'onkeyup': 'validationField("id_last_name", "Id_last_name")'
			}
		)
	)
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
