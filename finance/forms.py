import datetime
from decimal import Decimal

from django import forms
from django.core.validators import MinValueValidator


class TransactionForm(forms.Form):
    tx_type = forms.ChoiceField(widget=forms.HiddenInput(), choices=[("income", "Income"), ("expense", "Expense")])
    description = forms.CharField(
        label="Description",
        max_length=255,
        help_text="What was this expense for?",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "e.g., Lunch at restaurant, office supplies..."}
        ),
    )
    amount = forms.DecimalField(
        label="Amount",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("1.00"))],
        help_text="Enter amount in dollars",
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": "1.00", "placeholder": "0.00"}),
    )
    date = forms.DateField(
        label="Date",
        initial=datetime.date.today,
        help_text="When did this expense occur?",
        widget=forms.DateInput(attrs={"calss": "form-control", "type": "date"}),
    )
