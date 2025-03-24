from django.shortcuts import redirect, render
from django.db.models import Sum

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
    record_list = Record.objects.filter(confirmed=True).filter(user=pk)
    distance_sum = Record.objects.filter(confirmed=True).filter(user=pk).aggregate(Sum('distance'))
    print(distance_sum)

    return render(request,"run_record.html", {"context":record_list, "distance_sum":distance_sum})
