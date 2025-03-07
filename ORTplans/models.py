from django.db import models

# Create your models here.

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
    Upload_Elab = models.BooleanField(null=True)
    Remark = models.TextField(null=True)
    
    def __str__(self):
        res = ""
        res += str(self.JobNo) + ", "
        res += str(self.QRT) + ", "
        res += self.Product + ", "
        res += self.Customer + ", "
        res += self.PartNo + ", "
        res += self.Stage + ", "
        res += self.TestItem + ", "
        res += str(self.SampleSize) + ", "
        res += str(self.TestPeriod) + ", "
        res += self.Owner + ", "
        res += str(self.StartDate) + ", "
        res += str(self.EndDate) + ", "
        res += self.Status + ", "
        res += str(self.Upload_Elab) + ", "
        res += self.Remark
        return res

class TCheckouts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout_date = models.DateField()
    checkout_no = models.CharField(max_length=20)
    PartNo = models.CharField(max_length=15)
    TestItem = models.CharField(max_length=50, null=True)
    checkout_qty = models.DecimalField(max_digits=10, decimal_places=2)
    SN = models.TextField()
    DC = models.CharField(max_length=8)
    REV = models.CharField(max_length=10)
    Work_Order = models.CharField(max_length=40)
    Remarks = models.TextField(null=True)
    checkout_status = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        res = ""
        res += str(self.checkout_date) + ", "
        res += self.checkout_no + ", "
        res += self.PartNo + ", "
        res += self.TestItem + ", "
        res += str(self.checkout_qty) + ", "
        res += self.SN + ", "
        res += self.DC + ", "
        res += self.REV + ", "
        res += self.Work_Order + ", "
        res += self.Remarks + ", "
        res += self.checkout_status
        return res
