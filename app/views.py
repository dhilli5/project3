from django.shortcuts import render
from django.http import HttpResponse


def subbu(request):
    return HttpResponse('<h1>hello, my name is subbu</h1>')
def dhana(request):
    return HttpResponse('<h1>hello , my name is the dhana</h1>')

# Create your views here.
