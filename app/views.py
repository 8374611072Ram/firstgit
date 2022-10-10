from multiprocessing import context
from unicodedata import name
from django.shortcuts import render

# Create your views here.
def first_html(request):
    return render(request, 'first_html.html', context={'b' : 120,'a':100, 'c':150})
