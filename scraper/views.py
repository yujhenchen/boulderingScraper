from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'hello_world' : 'Hello world!'}
    return render(request, 'index.html', context) 
