from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    """This is home page route"""
    return HttpResponse('<h1> Blog Home page </h1>')

def about(request):
    """This is about us route"""
    return HttpResponse('<h1> About Us </h1>')

