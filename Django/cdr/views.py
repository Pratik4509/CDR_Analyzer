from django.shortcuts import render
from cdr.models import CDRdb

def Showdata(request):
    res=CDRdb.objects.all()
    return render(request,"display.html",{'CDRdb':res})