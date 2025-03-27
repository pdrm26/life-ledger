from django.urls import path

from .views import add_todo, delete_todo, edit_todo, todo_list

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path("add/", add_todo, name="add_todo"),
    path("edit/<int:pk>/", edit_todo, name="edit_todo"),
    path("delete/<int:pk>/", delete_todo, name="delete_todo"),
]
