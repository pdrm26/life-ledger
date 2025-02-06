from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    token = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user, self.token)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.text, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.text, self.amount)
