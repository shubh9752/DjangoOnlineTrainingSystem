from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def testpaper(request):
    que='What is the capital of France?'
    a='Paris'
    b='London'
    c='Berlin'
    d='Madrid'
    context={
        'que': que,
        'options':[c,b,a,d]
       
    }
    template=loader.get_template('testpaper.html')
    res= template.render(context, request)
    return HttpResponse(res)

def results(request):
    b = '<h1>Welcome to the Results Page</h1>'
    return HttpResponse(b)

# Create your views here.
