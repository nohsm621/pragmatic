from django.http import HttpResponse


# def: define function
from django.shortcuts import render


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')
