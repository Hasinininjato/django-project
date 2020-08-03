from django import forms


class FirstAppForm(forms.Form):
	inputText = forms.CharField(
		label='Text',
		widget=forms.TextInput(
			attrs={
				'class': 'form-group',
				'onkeyup': 'onFieldChanged()',
				'autocomplete': 'off',
			}
		)
	)
