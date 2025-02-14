from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField()
    password = forms.CharField(
        label='Password', max_length=50)
