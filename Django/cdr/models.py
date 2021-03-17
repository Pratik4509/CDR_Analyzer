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


class Max_Call(models.Model):
    CalledNo=models.IntegerField(primary_key=True)
    Total_Duration=models.IntegerField()
    total=models.IntegerField()
    class Meta:
        db_table="max_caller"

class MaxDuration(models.Model):
    CalledNo=models.CharField(primary_key=True,max_length=30)
    Total_Duration=models.IntegerField()
    total=models.IntegerField()
    class Meta:
        db_table="maxduration"

class CellId(models.Model):
    CellId=models.CharField(primary_key=True,max_length=30)
    Duration=models.IntegerField()
    No_of_Calls=models.IntegerField()
    Address=models.CharField(max_length=30)
    Latitude=models.BigIntegerField()
    Longitude=models.BigIntegerField()
    class Meta:
        db_table="cellidd"

class MaxIMEI(models.Model):
    IMEINo=models.BigIntegerField(primary_key=True)
    No_of_Calls=models.IntegerField()
    Total_Duration=models.IntegerField()
    First_Call=models.DateField()
    Last_Call=models.DateField()
    Total=models.IntegerField()
    class Meta:
        db_table="maximei"

