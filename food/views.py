from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def item(request):
    return HttpResponse("This is an item view.")