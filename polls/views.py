from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hello!</h1>");

def page1(request):
    return HttpResponse("<h1>page1</h1>");
