from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'login/index.html')


def login(request):
    return render(request, 'login/loginindex.html')


