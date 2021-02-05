from django.http import HttpResponse


# def: define function
def hello_world(request):
    return HttpResponse('Hello world')
