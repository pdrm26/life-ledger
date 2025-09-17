from django.contrib.auth.models import User
from django.db import models


class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.description, self.amount)


class Income(models.Model):
    description = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.description, self.amount)
