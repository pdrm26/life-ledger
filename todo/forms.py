from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "description", "deadline", "priority", "status")
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
