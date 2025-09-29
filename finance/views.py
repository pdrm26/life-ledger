from datetime import date
from json import JSONEncoder

from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .forms import TransactionForm
from .models import Expense, Income

fake_transactions = [
    {
        "id": 13,
        "type": "income",
        "description": "Tax Refund",
        "amount": 450.00,
        "date": date(2025, 3, 15),
    },
    {
        "id": 14,
        "type": "expense",
        "description": "Gym Membership",
        "amount": 39.99,
        "date": date(2025, 3, 16),
    },
    {
        "id": 15,
        "type": "expense",
        "description": "Online Subscription",
        "amount": 9.99,
        "date": date(2025, 3, 17),
    },
]

# Calculate totals for context
total_income = sum(t["amount"] for t in fake_transactions if t["type"] == "income")
total_expenses = sum(t["amount"] for t in fake_transactions if t["type"] == "expense")
net_balance = total_income - total_expenses

# Sort by date (newest first)
fake_transactions.sort(key=lambda x: x["date"], reverse=True)


def home_page(request):
    if request.method == "POST":
        user = get_object_or_404(User, id=request.user.id)
        form = TransactionForm(request.POST)
        if form.is_valid():
            tx_type = form.cleaned_data.pop("tx_type")
            if tx_type == "expense":
                Expense.objects.create(user=user, **form.cleaned_data)
            elif tx_type == "income":
                Income.objects.create(user=user, **form.cleaned_data)
    else:
        form = TransactionForm()

    context = {
        "form": form,
        "transactions": fake_transactions,
        "total_income": total_income,  # 5225.00
        "total_expenses": total_expenses,  # 611.63
        "net_balance": net_balance,  # 4613.37
    }
    return render(request, "home.html", context)


@csrf_exempt
def generalstat(request):
    if request.method == "GET":
        user = get_object_or_404(User, id=request.user.id)

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
