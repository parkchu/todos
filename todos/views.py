from django.shortcuts import render
from django.views.generic import ListView
from todos.models import todos
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class TodosMainView(ListView):
    model = todos


def add_todos(request):
    add_todo = request.POST['todo']
    pichu = request.POST['pichu']
    Todos = todos()
    Todos.todo = add_todo
    Todos.save()
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def finish_todo(request):
    todo = request.POST['pikachu']
    pichu = request.POST['pichu']
    todos.objects.filter(todo=todo).update(finish="completed")
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def notfinish_todo(request):
    todo = request.POST['pikachu']
    pichu = request.POST['pichu']
    todos.objects.filter(todo=todo).update(finish="")
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def del_todo(request):
    todo = request.POST['pikachu']
    pichu = request.POST['pichu']
    todos.objects.filter(todo=todo).delete()
    return HttpResponseRedirect(reverse('todos:{}'.format(pichu)))

def active(request):
    active_todo = todos.objects.filter(finish="")
    context = {'active_todo': active_todo}
    return render(request, 'todos/active.html', context)

def completed(request):
    completed_todo = todos.objects.filter(finish="completed")
    context = {'completed_todo': completed_todo}
    return render(request, 'todos/completed.html', context)