from django.shortcuts import redirect, render
from django.db.models import Sum
from django.core.paginator import Paginator

from record.models import Record

# Create your views here.

def runres(request):
    return render(request,"run_res.html")

def recordres(request):

    if request.method == "POST":
        record = Record()
        record.title = request.POST["title"]
        record.user = request.user
        record.record_date = request.POST["record_date"]
        record.image = request.FILES["image"]
        record.distance = request.POST["distance"]
        record.pace_m = request.POST["pace_m"]
        record.pace_s = request.POST["pace_s"]
        record.time_m = request.POST["time_m"]
        record.time_s = request.POST["time_s"]
        record.desc = request.POST["desc"]
        record.save()
        return render(request, "index.html")
    else:
        return render(request, "index.html")

def recordview(request,pk):

    month = request.GET.get('month')

    if month =="0" or month == None:
        month = "0"
        record_list = Record.objects.filter(user=pk).order_by('-record_date')
        distance_sum = Record.objects.filter(confirmed=True).filter(user=pk).aggregate(Sum('distance'))
        distance_sum_not = Record.objects.filter(user=pk).aggregate(Sum('distance'))
        
    else:
        record_list = Record.objects.filter(user=pk).filter(record_date__month=month)
        distance_sum = Record.objects.filter(confirmed=True).filter(user=pk).filter(record_date__month=month).aggregate(Sum('distance'))
        distance_sum_not = Record.objects.filter(user=pk).filter(record_date__month=month).aggregate(Sum('distance'))
    
    page = int(request.GET.get('p', 1)) #없으면 1로 지정
    paginator = Paginator(record_list, 3) #한 페이지 당 몇개 씩 보여줄 지 지정
    record_list = paginator.get_page(page)

    return render(request,"run_record.html", {"context":record_list, "distance_sum":distance_sum, "month": month, "distance_sum_not":distance_sum_not})

def recordUpdateView(request,pk,record_id):
    record = Record.objects.filter(user=pk).get(record_id=record_id)
    return render(request,"run_update.html", {"record_id":record_id, "record":record})

def recordUpdate(request,pk,record_id):
    record = Record.objects.filter(user=pk).get(record_id=record_id)
    if request.method == "POST":
        record.title = request.POST["title"]
        record.user = request.user
        record.record_date = request.POST["record_date"]
        if request.FILES.get("image") is not None:
            record.image = request.FILES["image"]
        record.distance = request.POST["distance"]
        record.pace_m = request.POST["pace_m"]
        record.pace_s = request.POST["pace_s"]
        record.time_m = request.POST["time_m"]
        record.time_s = request.POST["time_s"]
        record.desc = request.POST["desc"]
        record.save()
        return render(request, "index.html")
    else:
        return render(request, "index.html")