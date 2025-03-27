from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Todo


@csrf_exempt
def list_todos(request):
    status = request.GET.get("status")
    todos = Todo.objects.filter(status__iexact=status) if status else Todo.objects.all()

    return JsonResponse(list(todos.values()), safe=False)
