from django.shortcuts import render
from .models import Todo

# Create your views here.


def index(request):
    # Render all Todo
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'index.html', {'todos': todos})


def create_todo(request):
    # Creating a new Todo
    success = True
    try:
        title = request.POST.get('title')
        description = request.POST.get('description')
        print(f"${title} ${description}")
        todo = Todo.objects.create(title=title, description=description)
        todo.save()
    except Exception as error:
        print(f"Error Occured: ${error}")
        success = False
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-section.html', {'todos': todos, 'form': todo, 'success': success})


def mark_todo(request, pk):
    # Marking completed True
    success = True
    try:
        todo = Todo.objects.get(pk=pk)
        todo.completed = True
        todo.save()
    except Exception as error:
        print(f"Error Occured: ${error}")
        success = False
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos, 'success': success})


def delete_todo(request, pk):
    # Deleting a Todo
    success = True
    try:
        todo = Todo.objects.get(pk=pk)
        todo.delete()
    except Exception as error:
        print(f"Error Occured: ${error}")
        success = False
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos, 'success': success})
