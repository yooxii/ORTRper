from django.shortcuts import render

# Create your views here.
from ORTplans.models import TCheckouts
from rich import inspect


def index(request):

    return render(request=request, template_name="ortplans/index.html")


def checkouts(request):
    all_checkouts = TCheckouts.objects.all().values()
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


def edit_checkouts(request):
    # inspect(request.GET)
    if request.method == "GET":
        checkout = TCheckouts.objects.filter(id=request.GET.get("checkout_id"))
        data = checkout.values()[0]
        data["checkout_date"] = str(data["checkout_date"])
        context = {
            "checkout": data,
        }
        return render(
            request=request,
            template_name="ortplans/edit_checkouts.html",
            context=context,
        )
    else:
        return render(request=request, template_name="ortplans/checkouts.html")


def add_checkouts(request):
    context = {
        "checkout": {
            "id": 0,
        }
    }
    return render(
        request=request,
        template_name="ortplans/edit_checkouts.html",
        context=context,
    )


def save_edit_checkouts(request):
    if request.method == "POST":
        # 获取表单数据
        checkout_id = request.POST.get("checkout_id")
        checkout_date = request.POST.get("checkout_date")
        checkout_no = request.POST.get("checkout_no")
        PartNo = request.POST.get("PartNo")
        checkout_qty = request.POST.get("checkout_qty")
        TestItem = request.POST.get("TestItem")
        sn = request.POST.get("SN")
        dc = request.POST.get("DC")
        rev = request.POST.get("REV")
        Work_Order = request.POST.get("Work_Order")
        Remarks = request.POST.get("Remarks")

        cur = TCheckouts.objects.filter(id=checkout_id)
        if cur.exists():
            # 更新现有记录
            checkout, created = TCheckouts.objects.update_or_create(
                id=checkout_id,
                defaults={
                    "checkout_date": checkout_date,
                    "checkout_no": checkout_no,
                    "PartNo": PartNo,
                    "checkout_qty": checkout_qty,
                    "TestItem": TestItem,
                    "SN": sn,
                    "DC": dc,
                    "REV": rev,
                    "Work_Order": Work_Order,
                    "Remarks": Remarks,
                },
            )
        else:
            # 插入新记录
            checkout = TCheckouts(
                checkout_date=checkout_date,
                checkout_no=checkout_no,
                PartNo=PartNo,
                checkout_qty=checkout_qty,
                TestItem=TestItem,
                SN=sn,
                DC=dc,
                REV=rev,
                Work_Order=Work_Order,
                Remarks=Remarks,
            )
            checkout.save()
    return checkouts(request)


def delete_checkouts(request):
    if request.method == "GET":
        checkout_id = request.GET.get("checkout_id")
        TCheckouts.objects.filter(id=checkout_id).delete()
    return checkouts(request)
