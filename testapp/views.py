from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    a='<h1>Welcome to the Home Page</h1>'
    return HttpResponse(a);

def about(request):
    b='<h1>Welcome to the About Page</h1>'
    return HttpResponse(b);

def contact(request):
    c='<h1>Welcome to the Contact Page</h1>'
    return HttpResponse(c);