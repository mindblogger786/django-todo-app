from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo

# Create your views here.

def index(request):
    todos = ToDo.objects.all().order_by('-created_at')
    return render (request, 'todos/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        ToDo.objects.create(title=title)
    return redirect('index')

def complete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('index')

def delete_all_todos(request):
    ToDo.objects.all().delete()
    return redirect('index')
