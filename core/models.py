from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user, self.token)
