from django.shortcuts import render
from random import randint

def index(request):
    int = randint(0,30)
    return render(request, 'randnum_app/index.html', {'int':int})