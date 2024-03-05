# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('api/todos/', TodoItemListCreate.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', TodoItemRetrieveUpdateDestroy.as_view(), name='todo-item-detail'),
    path('', todo_list, name='todo-list'),
    # Add other URL patterns as needed
]
