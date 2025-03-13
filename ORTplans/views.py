from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from ORTplans.models import TCheckouts
from rich import inspect


def index(request):
    template = loader.get_template('ortplans/index.html')
    return HttpResponse(template.render(request=request))

def checkouts(request):
    template = loader.get_template('ortplans/checkouts.html')
    all_checkouts = TCheckouts.objects.all()
    inspect(all_checkouts)
    context = {
        'all_checkouts': all_checkouts,
    }
    return HttpResponse(template.render(context, request=request))

def import_checkouts(request):
    template = loader.get_template('ortplans/import_checkouts.html')
    return HttpResponse(template.render(request=request))

def export_checkouts(request):
    template = loader.get_template('ortplans/export_checkouts.html')
    return HttpResponse(template.render(request=request))

def edit_checkouts(request):
    template = loader.get_template('ortplans/edit_checkouts.html')
    return HttpResponse(template.render(request=request))

def delete_checkouts(request):
    template = loader.get_template('ortplans/delete.html')
    return HttpResponse(template.render(request=request))
