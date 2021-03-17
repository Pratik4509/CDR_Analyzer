from django.shortcuts import render
from cdr.models import CDRdb
from cdr.models import Max_Call
from cdr.models import MaxDuration
from cdr.models import CellId
from cdr.models import MaxIMEI
from django.http import HttpResponse


def Showdata(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=CDRdb.objects.raw('select id,CallingNo,CalledNo,CallType,CallDate,CallTime,CallDuration,FirstCellId,LastCellId,IMEINo,Circle from cdr_logs where CallDate between "'+fromdate+'" and "'+todate+'"')
        return render(request,'display.html',{"CDRdb":searchresult})
    else:
        res=CDRdb.objects.all()
        return render(request,'display.html',{"CDRdb":res})
def maxcall(request):
   # if request.method=="POST":
        #fromdate=request.POST.get('fromdate')
        #todate=request.POST.get('todate')
        #searchresult=Max_Call.objects.raw('SELECT DISTINCT (CalledNo),(SUM(Durration) over (PARTITION BY CalledNo)) as Total_Duration,(SUM(xyz) over (PARTITION BY CalledNo)) AS total FROM test order BY CalledNo')
       # return searchresult#render(request,'display.html',{"Max_Call":searchresult})
   # else:
        res=Max_Call.objects.all()
        return render(request,'MaxCaller.html',{"Max_Call":res})
def maxduration(request):
     # if request.method=="POST":
        #fromdate=request.POST.get('fromdate')
        #todate=request.POST.get('todate')
        #searchresult=Max_Call.objects.raw('SELECT DISTINCT (CalledNo),(SUM(Durration) over (PARTITION BY CalledNo)) as Total_Duration,(SUM(xyz) over (PARTITION BY CalledNo)) AS total FROM test order BY CalledNo')
       # return searchresult#render(request,'display.html',{"Max_Call":searchresult})
   # else:
        res=MaxDuration.objects.all()
        return render(request,'MaxDuration.html',{"MaxDuration":res}) 
def maxlocation(request):
    return render(request,'MaxLocation.html',)
def maximei(request):
    # if request.method=="POST":
    #    searchresult=CDRdb.objects.raw('SELECT IMEINo,(COUNT(IMEINo)) AS No_of_Calls,(SUM(CallDuration)) as Total_Duration,MIN(CallDate) AS First_Call,MAX(CallDate) AS Last_Call,(COUNT(DISTINCT(FirstCellId))) AS Total from cdr_logs GROUP BY IMEINo ORDER BY CallDate ASC')
     #   return render(request,'CellId.html',{"CDRdb":searchresult})
   # else:
    res=MaxIMEI.objects.all()
    return render(request,'MaxIMEI.html',{"MaxIMEI":res}) 
def cellid(request):
   # if request.method=="POST":
    #    searchresult=CDRdb.objects.raw('SELECT DISTINCT (FirstCellId) AS CellId,(SUM(CallDuration) over (PARTITION BY FirstCellId)) as Duration,(COUNT(FirstCellId) over (PARTITION BY firstCellId)) as No_of_Calls FROM cdr_logs order BY Duration DESC')
     #   return render(request,'CellId.html',{"CDRdb":searchresult})
   # else:
        res=CellId.objects.all()
        return render(request,'CellId.html',{"CellId":res})
def reset(request):
    if request.method=="POST":
        searchresult=CDRdb.objects.all()
        return searchresult
    else:
        res=CDRdb.objects.all()
        return res
def passdata(request):
    a=Showdata(request)
    b=maxcall(request)
    c=reset(request)
    d=cellid(request)
    e=maxduration(request)
    f=maximei(request)
    return render(request,'display.html',{"CDRdb":a,"Max_Call":b,"CRDdb":c,"CellId":d,"MaxDuration":e,"MaxIMEI":f})
