from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .forms import TransactionForm
from .models import Transaction


def home_page(request):
    if request.method == "POST":
        user = get_object_or_404(User, id=request.user.id)
        form = TransactionForm(request.POST)
        if form.is_valid():
            Transaction.objects.create(user=user, **form.cleaned_data)
    else:
        form = TransactionForm()

    context = {
        "form": form,
        "transactions": Transaction.objects.filter(user=user),
        "total_income": 10000,
        "total_expenses": 1,
        "net_balance": 2.2,
    }
    return render(request, "home.html", context)


@csrf_exempt
def generalstat(request):
    # if request.method == "GET":
    #     user = get_object_or_404(User, id=request.user.id)

    #        user_total_expense = Expense.objects.filter(user=user).aggregate(
    #            total_expense=Sum("amount", default=0), total_expense_count=Count("amount")
    #        )
    #        user_total_income = Income.objects.filter(user=user).aggregate(
    #            total_income=Sum("amount", default=0), total_income_count=Count("amount")
    #        )

    # return JsonResponse(
    #     {
    #         "status": "OK",
    #         "expense": user_total_expense,
    #         "income": user_total_income,
    #         "balance": user_total_income["total_income"] - user_total_expense["total_expense"],
    #     },
    #     encoder=JSONEncoder,
    # )
    return JsonResponse({"error": "Only GET request are allowed"}, status=400)
