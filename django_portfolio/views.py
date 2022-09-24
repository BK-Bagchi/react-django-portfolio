from django.shortcuts import render
from django.http import HttpResponse


def baseURL(request):
    return HttpResponse('<h1>React Django Portfolio Back end</h1>')
