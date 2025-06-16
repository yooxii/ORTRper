from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field


class CheckoutForm(forms.ModelForm):
    checkout_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="领用日期"
    )
    checkout_qty = forms.IntegerField(
        widget=forms.NumberInput(attrs={"min": 0}), label="领用数量"
    )

    class Meta:
        model = TCheckouts
        fields = [
            "checkout_no",
            "PartNo",
            "checkout_date",
            "DC",
            "checkout_qty",
            "REV",
            "Work_Order",
            "TestItem",
            "checkout_status",
            "SN",
            "Remarks",
        ]

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)

        data = args[0] if args else {}
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                    "value": data.get(name, ""),
                }
            )


class ScheduleForm(forms.ModelForm):
    # StartDate = forms.DateField(
    #     widget=forms.DateInput(attrs={"type": "date"}), label="开始日期"
    # )
    # EndDate = forms.DateField(
    #     widget=forms.DateInput(attrs={"type": "date"}), label="结束日期"
    # )
    # SampleSize = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={"min": 0}), label="样品数"
    # )

    class Meta:
        model = TSchedule
        fields = [
            "JobNo",
            "QRT",
            "Product",
            "Customer",
            "PartNo",
            "Stage",
            "TestItem",
            "SampleSize",
            "TestPeriod",
            "Owner",
            "StartDate",
            "EndDate",
            "Status",
            "Upload_Elab",
            "Remark",
        ]

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column("JobNo", css_class="form-group col-md-2 mb-0"),
                Column("QRT", css_class="form-group col-md-1 mb-0"),
                Column("Product", css_class="form-group col-md-3 mb-0"),
                Column("Customer", css_class="form-group col-md-3 mb-0"),
                Column("Stage", css_class="form-group col-md-3 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("PartNo", css_class="form-group col-md-3 mb-0"),
                Column("TestItem", css_class="form-group col-md-3 mb-0"),
                Column("SampleSize", css_class="form-group col-md-3 mb-0"),
                Column("TestPeriod", css_class="form-group col-md-3 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column(
                    Field(
                        "StartDate", css_class="form-group col-md-3 mb-0", type="date"
                    ),
                ),
                Column(
                    Field("EndDate", css_class="form-group col-md-3 mb-0", type="date"),
                ),
                Column("Status", css_class="form-group col-md-3 mb-0"),
                Column("Upload_Elab", css_class="form-group col-md-3 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("Owner", css_class="form-group col-md-6 mb-0"),
                Column("Remark", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Div(
                Submit(
                    "返回", "返回", css_class="button white", onclick="history.back(-1)"
                ),
                Submit("保存", "保存", css_class="button white"),
            ),
        )

        data = args[0] if args else {}
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "value": data.get(name, ""),
                }
            )
