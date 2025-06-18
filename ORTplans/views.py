from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest

# Create your views here.
from ORTplans.models import *
from ORTplans.ortplanforms import *


def index(request):
    return render(request, "ortplans/index.html")


################# Common Functions #################


def render_edit_form(
    request,
    model_class,
    form_class,
    object_id,
    template_name,
    redirect_view_name,
    title_text,
):
    """编辑函数模板

    Args:
        request (request): 网络请求
        model_class (model_class): 模型类
        form_class (form_class): 表单类
        object_id (int): 要编辑的对象ID
        template_name (str): 渲染的html模板名
        redirect_view_name (str): 重定向的视图名
        title_text (str): 网页标题

    Returns:
        (HttpResponse|redirect): 渲染的html或重定向
    """
    if request.method == "GET":
        obj = get_object_or_404(model_class, id=object_id)
        form = form_class(instance=obj)
        return render(request, template_name, {"title": title_text, "form": form})

    obj = get_object_or_404(model_class, id=object_id)
    form = form_class(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(redirect_view_name)
    else:
        return render(request, template_name, {"title": title_text, "form": form})


def render_add_form(request, form_class, template_name, redirect_view_name, title_text):
    """添加函数模板

    Args:
        request (request): 网络请求
        form_class (form_class): 表单类
        template_name (str): 渲染的html模板名
        redirect_view_name (str): 重定向的视图名
        title_text (str): 网页标题

    Returns:
        (HttpResponse|redirect): 渲染的html或重定向
    """

    if request.method == "GET":
        form = form_class()
        return render(request, template_name, {"title": title_text, "form": form})

    form = form_class(request.POST)
    if form.is_valid():
        form.save()
        return redirect(redirect_view_name)
    else:
        return render(request, template_name, {"title": title_text, "form": form})


def handle_delete(request, model_class, object_id, redirect_view_name):
    obj = get_object_or_404(model_class, id=object_id)
    obj.delete()
    return redirect(redirect_view_name)


################# Checkouts #################


def checkouts(request):
    all_checkouts = TCheckouts.objects.all()
    context = {
        "all_checkouts": all_checkouts,
    }
    return render(request, "ortplans/checkouts.html", context)


def import_checkouts(request):
    return render(request, "ortplans/import_checkouts.html")


def export_checkouts(request):
    return render(request, "ortplans/export_checkouts.html")


def edit_checkouts(request, checkout_id=0):
    return render_edit_form(
        request,
        TCheckouts,
        CheckoutForm,
        checkout_id,
        "ortplans/edit_table1.html",
        "checkouts",
        "领用编辑",
    )


def add_checkouts(request):
    return render_add_form(
        request, CheckoutForm, "ortplans/edit_table1.html", "checkouts", "领用添加"
    )


def delete_checkouts(request, checkout_id):
    return handle_delete(request, TCheckouts, checkout_id, "checkouts")


################# Schedules #################


def schedules(request):
    all_schedules = TSchedule.objects.all()
    context = {
        "all_schedules": all_schedules,
    }
    return render(request, "ortplans/schedules.html", context)


def import_schedules(request):
    return render(request, "ortplans/import_schedules.html")


def export_schedules(request):
    return render(request, "ortplans/export_schedules.html")


def edit_schedules(request, schedule_id=0):
    template_name = "ortplans/edit_table1.html"
    redirect_view_name = "schedules"
    title_text = "排程编辑"

    if request.method == "GET":
        obj = get_object_or_404(TSchedule, id=schedule_id)
        form = ScheduleForm(instance=obj)
        return render(request, template_name, {"title": title_text, "form": form})

    obj = get_object_or_404(TSchedule, id=schedule_id)
    form = ScheduleForm(request.POST, instance=obj)
    if form.is_valid():
        form.data.update({"id": schedule_id})
        form.save()
        return redirect(redirect_view_name)
    else:
        return render(request, template_name, {"title": title_text, "form": form})


def add_schedules(request):
    template_name = "ortplans/edit_table1.html"
    redirect_view_name = "schedules"
    title_text = "排程编辑"

    if request.method == "GET":
        form = ScheduleForm()
        return render(request, template_name, {"title": title_text, "form": form})

    form = ScheduleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(redirect_view_name)
    else:
        return render(request, template_name, {"title": title_text, "form": form})


def delete_schedules(request, schedule_id):
    return handle_delete(request, TSchedule, schedule_id, "schedules")


################# Technicians #################


def technicians(request):
    all_technicians = TTechnician.objects.all()
    context = {
        "all_technicians": all_technicians,
        "title": "测试人员管理",
    }
    return render(request, "ortplans/technicians.html", context)


def edit_technicians(request, technician_id=0):
    return render_edit_form(
        request,
        TTechnician,
        TechnicianForm,
        technician_id,
        "ortplans/edit_table1.html",
        "technicians",
        "测试人员编辑",
    )


def add_technicians(request):
    return render_add_form(
        request,
        TechnicianForm,
        "ortplans/edit_table1.html",
        "technicians",
        "测试人员添加",
    )


def delete_technicians(request, technician_id):
    return handle_delete(request, TTechnician, technician_id, "technicians")


################# TestItems #################


def testitems(request):
    all_testitems = TTestItem.objects.all()
    context = {
        "all_testitems": all_testitems,
        "title": "测试项目管理",
    }
    return render(request, "ortplans/testitems.html", context)


def edit_testitems(request, testitem_id=0):
    return render_edit_form(
        request,
        TTestItem,
        TestItemForm,
        testitem_id,
        "ortplans/edit_table1.html",
        "testitems",
        "测试项目编辑",
    )


def add_testitems(request):
    return render_add_form(
        request,
        TestItemForm,
        "ortplans/edit_table1.html",
        "testitems",
        "测试项目添加",
    )


def delete_testitems(request, testitem_id):
    return handle_delete(request, TTestItem, testitem_id, "testitems")


################# CustProducts #################


def custproducts(request):
    all_customers = TCustCode.objects.all()
    all_products = TProductType.objects.all()
    context = {
        "all_customers": all_customers,
        "all_products": all_products,
        "title": "客户与产品管理",
    }
    return render(request, "ortplans/custproducts.html", context)


def edit_customers(request, customer_id=0):
    return render_edit_form(
        request,
        TCustCode,
        CustCodeForm,
        customer_id,
        "ortplans/edit_table1.html",
        "custproducts",
        "客户编辑",
    )


def add_customers(request):
    return render_add_form(
        request, CustCodeForm, "ortplans/edit_table1.html", "custproducts", "客户添加"
    )


def delete_customers(request, customer_id):
    return handle_delete(request, TCustCode, customer_id, "custproducts")


def edit_products(request, product_id=0):
    return render_edit_form(
        request,
        TProductType,
        ProductTypeForm,
        product_id,
        "ortplans/edit_table1.html",
        "custproducts",
        "产品编辑",
    )


def add_products(request):
    return render_add_form(
        request,
        ProductTypeForm,
        "ortplans/edit_table1.html",
        "custproducts",
        "产品添加",
    )


def delete_products(request, product_id):
    return handle_delete(request, TProductType, product_id, "custproducts")
