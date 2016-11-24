from django.shortcuts import render

# Create your views here.

def design(request):
    return render(request, 'buy/design.html',{})

def index(request):
    return render(request, 'buy/index.html',{})