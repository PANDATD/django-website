from django.shortcuts import render
from django.http import HttpResponse 
"""
Notes :- 

    render used to render templates 
    HttpResponse is used to Write Html response on site.

"""

def home(request):
    """This is home page view"""
    return HttpResponse('<h1> Blog Home page </h1>')

def about(request):
    """This is about page view"""
    return HttpResponse('<h1> About Us </h1>')

