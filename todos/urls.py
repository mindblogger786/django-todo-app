from django.urls import path
from .views import index, add_todo, complete_todo, delete_todo, delete_all_todos

urlpatterns = [
    path('', index, name='index'),
    path('/add_todo', add_todo, name='add_todo'),
    path('/complete_todo/<int:id>', complete_todo, name='complete_todo'),
    path('/delete_todo/<int:id>', delete_todo, name='delete_todo'),
    path('/delete_all_todos', delete_all_todos, name='delete_all_todos'),
]
