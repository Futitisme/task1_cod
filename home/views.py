from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    cod = ''
    for i in range(0,4): 
        cod += str(random.randint(0,9))
    return render(request, "index.html", {'cod':cod})
