from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import token_generator
from django.contrib.auth.models import User
from .models import Token


def home_view(request):
    return render(request, "home.html")


@csrf_exempt
def register_account(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    token = token_generator()

    user = User.objects.create(
        username=username, email=email, password=password)
    Token.objects.create(token=token, user=user)

    return JsonResponse({'status': "ok", "token": token})


@csrf_exempt
def login_account(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.get(username=username, password=password)
    token = Token.objects.get(user=user)

    return JsonResponse({'status': 'ok', 'token': token.token, })
