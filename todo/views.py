from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from core.models import Token

from .forms import TodoForm
from .models import Todo


@csrf_exempt
def todo_list(request):
    status = request.GET.get("status")
    todos = Todo.objects.filter(status__iexact=status) if status else Todo.objects.all()
    return render(request, "todo/todo_list.html", context={"todos": todos})


def add_todo(request):
    if request.method == "POST":
        try:
            user_token = request.session["user_token"]
        except KeyError:
            return HttpResponse("<p>you are not logged in</p>")

        token = Token.objects.get(token=user_token)

        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = token.user
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo/add_todo.html", context={"form": form})


def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    return render(request, "todo/edit_todo.html", context={"form": TodoForm(instance=todo)})


def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    # TODO: show the allert for success
    return redirect("todo_list")
