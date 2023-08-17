from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, this is the index view")

def pathview(request, name, id):
    return HttpResponse(f"The name {name} and the id {id}")