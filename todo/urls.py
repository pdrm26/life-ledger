from django.urls import path

from .views import list_todos

urlpatterns = [path("list", list_todos, name="todo_list")]
