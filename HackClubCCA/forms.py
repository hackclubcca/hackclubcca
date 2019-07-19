from django import forms


class EmailForm(forms.Form):
    email = forms.CharField(max_length=100,
    label='',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'enter your email',
            'class': 'green-text'
        })
    )