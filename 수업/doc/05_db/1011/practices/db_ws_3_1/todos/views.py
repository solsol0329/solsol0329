from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    # todos = Todo.objects.all()
    todos = request.user.todo_set.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            form.save()
            # todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)


def toggle(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    todo = Todo.objects.get(pk=pk)
    if request.user == todo.author:
        todo.completed = not todo.completed
        todo.save()
    return redirect('todos:index')


def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')    
    
    todo = Todo.objects.get(pk=pk)
    if request.user == todo.author:
        todo.delete()
    return redirect('todos:index')