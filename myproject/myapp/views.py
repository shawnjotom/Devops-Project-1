from django.shortcuts import render
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemListCreate(generics.ListCreateAPIView):
   queryset = TodoItem.objects.all()
   serializer_class = TodoItemSerializer

class TodoItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
   queryset = TodoItem.objects.all()
   serializer_class = TodoItemSerializer

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})
