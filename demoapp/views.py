# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.


def home(request):
    # return HttpResponse("hello world") #view
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html", {'result': obj,'team' : obj2})  # template

# def about(request):
#     return render(request,"about.html") #2nd template


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y

#     return render(request, "add.html",  {'num1': x, 'num2': y, 'result': res})
