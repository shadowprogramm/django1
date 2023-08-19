from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def index(request):
    return HttpResponse("Hello, this is the index view")

def pathview(request, name, id):
    if request.method == 'GET':
        return HttpResponse(f"The name {name} and the id {id}")
    
    return HttpResponse(f"Post request for {name}")



def informations(request, year):
    return HttpResponse(f'Information {year}')

class Operations(View):
    def get(self, request):
        return HttpResponse('Get')
    
    def post(self, request):
        return HttpResponse('Post')