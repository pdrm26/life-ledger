from json import JSONEncoder

from django.contrib.auth.models import User
from django.db.models import Count, Sum
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

        text = request.POST.get("text")
        amount = request.POST.get("amount")
        date = request.POST.get("date", timezone.now())

        Income.objects.create(text=text, amount=amount, user=user, date=date)
        return JsonResponse({"status": "ok"}, status=200)
    return JsonResponse({"error": "Only POST request are allowed"}, status=400)


@csrf_exempt
def generalstat(request):
    if request.method == "GET":
        user_token = request.headers.get("Token")
        user = get_object_or_404(User, token__token=user_token)

        user_total_expense = Expense.objects.filter(user=user).aggregate(
            total_expense=Sum("amount", default=0), total_expense_count=Count("amount")
        )
        user_total_income = Income.objects.filter(user=user).aggregate(
            total_income=Sum("amount", default=0), total_income_count=Count("amount")
        )

        return JsonResponse(
            {
                "status": "OK",
                "expense": user_total_expense,
                "income": user_total_income,
                "balance": user_total_income["total_income"] - user_total_expense["total_expense"],
            },
            encoder=JSONEncoder,
        )
    return JsonResponse({"error": "Only GET request are allowed"}, status=400)
