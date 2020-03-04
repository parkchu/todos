from django.shortcuts import render
from django.views.generic import ListView
from todos.models import todos
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def todos_list(request):
    todo_list = todos.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todos/todos_list.html', context)


def add_todos(request):
    add_todo = request.POST['todo']
    pichu = request.POST['pichu']
    Todos = todos()
    Todos.todo = add_todo
    Todos.save()
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def finish_todo(request):
    todo_id = request.POST['pikachu']
    pichu = request.POST['pichu']
    todos.objects.filter(id=todo_id).update(completed=True)
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def notfinish_todo(request):
    todo_id = request.POST['pikachu']
    pichu = request.POST['pichu']
    todos.objects.filter(id=todo_id).update(completed=False)
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def del_todo(request):
    todo_id = request.POST['pikachu']
    pichu = request.POST['pichu']
    todos.objects.filter(id=todo_id).delete()
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def active(request):
    active_todo = todos.objects.filter(completed=False)
    context = {'todo_list': active_todo}
    return render(request, 'todos/todos_list.html', context)

def completed(request):
    completed_todo = todos.objects.filter(completed=True)
    context = {'todo_list': completed_todo}
    return render(request, 'todos/todos_list.html', context)