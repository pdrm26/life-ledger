from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    class TransactionTypes(models.TextChoices):
        INCOME = "income"
        EXPENSE = "expense"

    description = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tx_type = models.CharField(choices=TransactionTypes, default="income", max_length=7)

    def __str__(self):
        return "{} -> {} - {} - {}".format(self.tx_type, self.date, self.description, self.amount)
