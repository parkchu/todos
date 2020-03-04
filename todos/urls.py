from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.TodosMainView.as_view(), name='index'),
    path('add_todos/', views.add_todos, name='add_todos'),
    path('finish_todo/', views.finish_todo, name='finish_todo'),
    path('notfinish_todo/', views.notfinish_todo, name='notfinish_todo'),
    path('del_todo/', views.del_todo, name='del_todo'),
    path('active/', views.active, name='active'),
    path('completed/', views.completed, name='completed'),
]