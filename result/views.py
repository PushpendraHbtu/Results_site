# this views page create by me 

from django.shortcuts import render


# create your views here.

def index (request):
    return render(request,'index.html')