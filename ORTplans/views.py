from django.shortcuts import render

# Create your views here.
from ORTplans.models import TCheckouts
from rich import inspect


def index(request):

    return render(request=request, template_name="ortplans/index.html")


def checkouts(request):
    all_checkouts = TCheckouts.objects.all()
    inspect(all_checkouts)
    context = {
        "all_checkouts": all_checkouts,
    }
    return render(
        request=request, template_name="ortplans/checkouts.html", context=context
    )


def import_checkouts(request):

    return render(request=request, template_name="ortplans/import_checkouts.html")


def export_checkouts(request):

    return render(request=request, template_name="ortplans/export_checkouts.html")


def edit_checkouts(request):

    return render(request=request, template_name="ortplans/edit_checkouts.html")


def delete_checkouts(request):

    return render(request=request, template_name="ortplans/delete.html")
