# file that contains all the endpoints for the API
from django.http import JsonResponse
from .models import TodoItem
from .serializers import TodoSerializer

def todo_list(request):
    # get all the todos
    # serialize them
    # return a json response
    todos = TodoItem.objects.all()
    serializer = TodoSerializer(todos, many=True).data
    return JsonResponse([{"data": serializer, "status": "ok"}], safe=False)
