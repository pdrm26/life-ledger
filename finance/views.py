from datetime import date
from json import JSONEncoder

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import ExpenseForm
from .models import Expense, Income


def home_page(request):
    return render(request, "home.html")


@csrf_exempt
@login_required
def submit_expense(request):
    # Sample transaction list
    fake_transactions = [
        {
            "id": 1,
            "type": "income",
            "description": "Salary - March 2025",
            "amount": 3500.00,
            "date": date(2025, 3, 1),
        },
        {
            "id": 2,
            "type": "expense",
            "description": "Grocery Shopping",
            "amount": 85.50,
            "date": date(2025, 3, 2),
        },
        {
            "id": 3,
            "type": "expense",
            "description": "Gas Bill",
            "amount": 120.00,
            "date": date(2025, 3, 3),
        },
        {
            "id": 4,
            "type": "income",
            "description": "Freelance Project",
            "amount": 750.00,
            "date": date(2025, 3, 5),
        },
        {
            "id": 5,
            "type": "expense",
            "description": "Coffee Shop",
            "amount": 12.50,
            "date": date(2025, 3, 6),
        },
        {
            "id": 6,
            "type": "expense",
            "description": "Internet Bill",
            "amount": 65.00,
            "date": date(2025, 3, 7),
        },
        {
            "id": 7,
            "type": "income",
            "description": "Investment Returns",
            "amount": 225.00,
            "date": date(2025, 3, 8),
        },
        {
            "id": 8,
            "type": "expense",
            "description": "Restaurant Dinner",
            "amount": 45.75,
            "date": date(2025, 3, 9),
        },
        {
            "id": 9,
            "type": "expense",
            "description": "Car Insurance",
            "amount": 180.00,
            "date": date(2025, 3, 10),
        },
        {
            "id": 10,
            "type": "income",
            "description": "Side Business",
            "amount": 300.00,
            "date": date(2025, 3, 12),
        },
        {
            "id": 11,
            "type": "expense",
            "description": "Pharmacy",
            "amount": 28.90,
            "date": date(2025, 3, 13),
        },
        {
            "id": 12,
            "type": "expense",
            "description": "Movie Tickets",
            "amount": 24.00,
            "date": date(2025, 3, 14),
        },
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

    # Context for your Django view
    if request.method == "POST":
        user = get_object_or_404(User, id=request.user.id)
        form = ExpenseForm(request.POST)
        if form.is_valid():
            Expense.objects.create(user=user, **form.cleaned_data)

    if request.method == "GET":
        form = ExpenseForm()

    context = {
        "form": form,
        "transactions": fake_transactions,
        "total_income": total_income,  # 5225.00
        "total_expenses": total_expenses,  # 611.63
        "net_balance": net_balance,  # 4613.37
    }
    return render(request, "expense.html", context)


@csrf_exempt
@login_required
def submit_income(request):
    if request.method == "POST":
        user = get_object_or_404(User, id=request.user.id)
        text = request.POST.get("text")
        amount = request.POST.get("amount")
        date = request.POST.get("date", timezone.now())

        Income.objects.create(text=text, amount=amount, user=user, date=date)
        return JsonResponse({"status": "ok"}, status=200)
    return JsonResponse({"error": "Only POST request are allowed"}, status=400)


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
