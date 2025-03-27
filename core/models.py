from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


class Token(models.Model):
    token = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(length=48)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.user, self.token)
