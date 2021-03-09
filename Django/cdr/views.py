from django.shortcuts import render
from cdr.models import CDRdb
from cdr.models import Max_Call
def Showdata(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=CDRdb.objects.raw('select id,CallingNo,CalledNo,CallType,CallDate,CallTime,CallDuration,FirstCellId,LastCellId,IMEINo,Circle from cdr_logs where CallDate between "'+fromdate+'" and "'+todate+'"')
        return searchresult#render(request,'display.html',{"CDRdb":searchresult})
    else:
        res=CDRdb.objects.all()
        return res#render(request,'display.html',{"CDRdb":res})
def maxcall(request):
   # if request.method=="POST":
        #fromdate=request.POST.get('fromdate')
        #todate=request.POST.get('todate')
        #searchresult=Max_Call.objects.raw('SELECT DISTINCT (CalledNo),(SUM(Durration) over (PARTITION BY CalledNo)) as Total_Duration,(SUM(xyz) over (PARTITION BY CalledNo)) AS total FROM test order BY CalledNo')
       # return searchresult#render(request,'display.html',{"Max_Call":searchresult})
   # else:
        res=Max_Call.objects.all()
        return res#render(request,'display.html',{"Max_Call":res})
#def imei(request):
   # if request.method=="POST":
    #    searchresult=CDRdb.objects.raw('SELECT DISTINCT (IMEINo),(COUNT(IMEINo) over (PARTITION BY IMEINo)) as Total,(SUM(CallDuration) over (PARTITION BY IMEINo)) as Total_Duration FROM cdr_logs order BY IMEINo')
     #   return searchresult
   # else:
    #    res=CDRdb.objects.all()
     #   return res
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
    return render(request,'display.html',{"CDRdb":a,"Max_Call":b,"CRDdb":c})
   
