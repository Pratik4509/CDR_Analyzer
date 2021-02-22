from django.db import connections
from django.db import models

class CDRdb(models.Model):

    CallingNo=models.IntegerField()
    CalledNo=models.IntegerField()
    CallType=models.CharField(max_length=30)
    CallDate=models.DateField()
    CallTime=models.TimeField()
    CallDuration=models.IntegerField()
    FirstCellId=models.CharField(max_length=30)
    LastCellId=models.CharField(max_length=30)
    IMEINo=models.BigIntegerField()
    Circle=models.CharField(max_length=30)
    class Meta:
        db_table="cdr_logs"
