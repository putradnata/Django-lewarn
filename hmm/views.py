from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request)
#     return render()

def index(request):
    context = {
        'addressTitle' : '666 Ticketing',
    }
    
    return render(request, 'Homepage/index.html', context)
