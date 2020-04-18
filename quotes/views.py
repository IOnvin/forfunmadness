from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def srinu(request):
    return render(request, 'srinu.html')


def srinu2(request):
    return render(request, 'srinu2.html')


def pratyu(request):
    return render(request, 'pratyu.html')


def pratyu2(request):
    return render(request, 'pratyu2.html')


def venki(request):
    return render(request, 'venki.html')