from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .utils import token_generator
from django.contrib.auth.models import User
from .models import Token
from .forms import RegisterForm


def home_view(request):
    return render(request, "home.html")


@csrf_exempt
def register_account(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            token = token_generator()

            user = User.objects.create(
                username=username, email=email, password=password)
            Token.objects.create(token=token, user=user)

            return HttpResponseRedirect("/")

    if request.method == "GET":
        form = RegisterForm()

    return render(request, "core/account/register.html", {"form": form})


@csrf_exempt
def login_account(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.get(username=username, password=password)
    token = Token.objects.get(user=user)

    return JsonResponse({'status': 'ok', 'token': token.token, })
