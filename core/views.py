from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, RegisterForm
from .models import Token


@csrf_exempt
def register_account(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            token = Token.objects.create(user=user)

            request.session["user_token"] = token.token

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

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")
            return render(request, "core/account/register.html", {"form": form})
    if request.method == "GET":
        if request.session.get("user_token"):
            return HttpResponseRedirect("/")
        form = LoginForm()

    return render(request, "core/account/login.html", {"form": form})
