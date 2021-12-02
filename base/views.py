from django.http.response import HttpResponseGone
from django.shortcuts import render
from django.http import HttpResponse


def taskList(request):
    return HttpResponse('To Do List')
