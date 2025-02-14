from django import forms
from django_recaptcha.fields import ReCaptchaField


class RegisterForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField()
    password = forms.CharField(
        label='Password', max_length=50)
    captcha = ReCaptchaField()


class LoginForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=50)
    password = forms.CharField(label="Password", max_length=50)
    captcha = ReCaptchaField()
