from django.http.response import HttpResponseGone
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from base.models import Task


class TaskList(ListView):
    model = Task
    # mudar o nome do queryset do listview, no caso o queryset seria os items do model
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
