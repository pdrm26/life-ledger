from datetime import datetime
from json import loads

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Expense, Income


@csrf_exempt
def submit_expense(request):
    if request.method == "POST":
        user_token = request.headers.get("Token")
        user = get_object_or_404(User, token__token=user_token)

        text = request.POST.get("text")
        amount = request.POST.get("amount")
        date = request.POST.get("date", timezone.now())

        Expense.objects.create(text=text, amount=amount, user=user, date=date)
        return JsonResponse({"status": "ok"}, status=200)

    return JsonResponse({"error": "only POST request are allowed"}, status=400)


@csrf_exempt
def submit_income(request):
    if request.method == "POST":
        user_token = request.headers.get("Token")
        user = get_object_or_404(User, token__token=user_token)
        body = loads(request.body.decode("utf-8"))
        if "date" not in body:
            date = datetime.now()
        Income.objects.create(text=body.get("text"), amount=body.get("amount"), user=user, date=date)
        return JsonResponse({"status": "ok"}, status=200)
    return JsonResponse({"status": "nok"}, status=400)
