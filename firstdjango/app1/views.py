from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import DemoForm, DbToForm
# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test


def test(user):
    return True


@user_passes_test(test)
def index(request):
    if request.user.is_anonymous():
        print('Not logged')
    return HttpResponse("Hello, this is the index view")

def pathview(request, name, id):
    if request.method == 'GET':
        return HttpResponse(f"The name {name} and the id {id}")
    
    return HttpResponse(f"Post request for {name}")


@login_required
def informations(request, year):
    return HttpResponse(f'Information {year}')

class FormView(View):
    def get(self, request):
        form = DbToForm()
        return render(request, 'form.html', {'form': form})
    
    def post(self, request):
        form = DbToForm(request.POST)
        if form.is_valid:
            form.save()
    
        return HttpResponse('Form')