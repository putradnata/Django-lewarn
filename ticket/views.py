from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request)
#     return render()

def index(request):
    context = {
        'addressTitle' : 'Tickets Page',
        'pageTitle' : 'Ticket Data',
    }
    
    return render(request, 'ticket/index.html', context)

def create(request):
    return HttpResponse('<h1>Add Data Will be here later</h1>')

def edit(request):
    return HttpResponse('<h1>Edit Data Will be here later</h1>')
