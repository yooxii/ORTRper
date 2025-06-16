from django.shortcuts import render, redirect

# Create your views here.
from ORTplans.models import *
from ORTplans.ortplanforms import *
from rich import inspect


def index(request):

    return render(request=request, template_name="ortplans/index.html")


################# Checkouts #################


def checkouts(request):
    all_checkouts = TCheckouts.objects.all()
    # inspect(all_checkouts)
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


def edit_checkouts(request, checkout_id=0):
    if request.method == "GET":
        checkout = TCheckouts.objects.filter(id=checkout_id).values()[0]
        checkout["checkout_date"] = checkout["checkout_date"].strftime("%Y-%m-%d")
        form = CheckoutForm(checkout)
        return render(
            request=request,
            template_name="ortplans/edit_checkouts.html",
            context={
                "form": form,
            },
        )

    checkout = TCheckouts.objects.get(id=checkout_id)
    form = CheckoutForm(data=request.POST, instance=checkout)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    else:
        print(form.errors)
        return render(
            request=request,
            template_name="ortplans/edit_checkouts.html",
            context={"form": form, "error": True},
        )
    return redirect("/ORTplans/checkouts")


def add_checkouts(request):
    if request.method == "GET":
        form = CheckoutForm()
        context = {
            "checkout": {
                "id": 0,
            },
            "form": form,
        }
        return render(
            request=request,
            template_name="ortplans/edit_checkouts.html",
            context=context,
        )

    form = CheckoutForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    else:
        print(form.errors)
        return render(
            request=request,
            template_name="ortplans/edit_checkouts.html",
            context={"form": form, "error": True},
        )
    return redirect("/ORTplans/checkouts")


def delete_checkouts(request, checkout_id):
    TCheckouts.objects.filter(id=checkout_id).delete()
    return redirect("/ORTplans/checkouts")


################# Schedules #################


def schedules(request):
    all_schedules = TSchedule.objects.all()
    # inspect(all_schedules)
    context = {
        "all_schedules": all_schedules,
    }
    return render(
        request=request, template_name="ortplans/schedules.html", context=context
    )


def import_schedules(request):

    return render(request=request, template_name="ortplans/import_schedules.html")


def export_schedules(request):
    return render(request=request, template_name="ortplans/export_schedules.html")


def edit_schedules(request, schedule_id=0):
    if request.method == "GET":
        schedule = TSchedule.objects.filter(id=schedule_id).first()
        form = ScheduleForm(instance=schedule)
        return render(
            request=request,
            template_name="ortplans/edit_schedules.html",
            context={
                "form": form,
            },
        )

    schedule = TSchedule.objects.get(id=schedule_id)
    form = ScheduleForm(data=request.POST, instance=schedule)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    else:
        print(form.errors)
        return render(
            request=request,
            template_name="ortplans/edit_schedules.html",
            context={"form": form, "error": True},
        )
    return redirect("/ORTplans/schedules")


def add_schedules(request):
    if request.method == "GET":
        form = ScheduleForm()
        context = {
            "schedule": {
                "id": 0,
            },
            "form": form,
        }
        return render(
            request=request,
            template_name="ortplans/edit_schedules.html",
            context=context,
        )

    form = ScheduleForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    else:
        print(form.errors)
        return render(
            request=request,
            template_name="ortplans/edit_schedules.html",
            context={"form": form, "error": True},
        )
    return redirect("/ORTplans/schedules")


def delete_schedules(request, schedule_id):
    TSchedule.objects.filter(id=schedule_id).delete()
    return redirect("/ORTplans/schedules")


################# Technicians #################


def technicians(request):
    return render(request=request, template_name="ortplans/technicians.html")
