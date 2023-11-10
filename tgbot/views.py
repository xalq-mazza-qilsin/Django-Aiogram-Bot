from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest):
    return HttpResponse('Hello world')
