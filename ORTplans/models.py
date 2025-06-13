from django.db import models


class TSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    JobNo = models.IntegerField()
    QRT = models.BooleanField(default=False)
    Product = models.CharField(max_length=25)
    Customer = models.CharField(max_length=15)
    PartNo = models.CharField(max_length=25)
    Stage = models.CharField(max_length=5)
    TestItem = models.CharField(max_length=50)
    SampleSize = models.IntegerField()
    TestPeriod = models.IntegerField()
    Owner = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Status = models.CharField(max_length=10)
    Upload_Elab = models.BooleanField(null=True, blank=True)
    Remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return (
            f"{self.JobNo}, {self.QRT}, {self.Product}, {self.Customer}, "
            f"{self.PartNo}, {self.Stage}, {self.TestItem}, {self.SampleSize}, "
            f"{self.TestPeriod}, {self.Owner}, {self.StartDate}, "
            f"{self.EndDate}, {self.Status}, {self.Upload_Elab}, {self.Remark}"
        )


class TCheckouts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout_date = models.DateField()
    checkout_no = models.CharField(max_length=20)
    PartNo = models.CharField(max_length=15)
    TestItem = models.CharField(max_length=50, null=True, blank=True)
    checkout_qty = models.IntegerField()
    SN = models.TextField(unique=True)
    DC = models.CharField(max_length=8)
    REV = models.CharField(max_length=10)
    Work_Order = models.CharField(max_length=40)
    Remarks = models.TextField(null=True, blank=True)
    checkout_status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.checkout_date}, {self.checkout_no}, {self.PartNo}, "
            f"{self.TestItem}, {self.checkout_qty}, {self.SN}, {self.DC}, "
            f"{self.REV}, {self.Work_Order}, {self.Remarks}, {self.checkout_status}"
        )
