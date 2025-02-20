from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, RegisterForm
from .models import Token


def home_view(request):
    return render(request, "home.html")


@csrf_exempt
def register_account(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create(username=username, email=email, password=password)
            Token.objects.create(user=user)

            return HttpResponseRedirect("/")

    if request.method == "GET":
        form = RegisterForm()

    return render(request, "core/account/register.html", {"form": form})


@csrf_exempt
def login_account(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # TODO: handle when you cant find the user

            user = User.objects.get(username=username, password=password)
            token = Token.objects.get(user=user)
            return render(request, "core/account/login.html", {"form": form, "token": token.token})

    if request.method == "GET":
        form = LoginForm()

    return render(request, "core/account/login.html", {"form": form})
