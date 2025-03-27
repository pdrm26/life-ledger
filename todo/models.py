from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    class Priority(models.TextChoices):
        LOW = "LOW", "Low Priority"
        MEDIUM = "MEDIUM", "Medium Priority"
        HIGH = "HIGH", "High Priority"
        URGENT = "URGENT", "Urgent Priority"

    class Status(models.TextChoices):
        BACKLOG = "BACKLOG", "Backlog"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    description = models.TextField(null=True, blank=True, validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.BACKLOG)

    def is_overdue(self):
        return timezone.now() > self.deadline and self.status != self.Status.COMPLETED

    def mark_complete(self):
        self.status = self.Status.COMPLETED
        self.completed_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
