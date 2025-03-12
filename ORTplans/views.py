from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('ortplans/index.html')
    return HttpResponse(template.render(request=request))

def checkouts(request):
    template = loader.get_template('ortplans/checkouts.html')
    return HttpResponse(template.render(request=request))