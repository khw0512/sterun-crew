from collections import defaultdict
import json
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse 
from django.core import serializers
from django.db.models import Q
from django.db.models import Max
from datetime import datetime

from marathon.models import *

def marathon_list(request):
    marathon = MarathonReg.objects.select_related("marathon").order_by("marathon_id")

    grouped = defaultdict(list)
    for item in marathon.values("id","marathon", "marathon__marathon_id","marathon__title", "user__username", "user__first_name", "user__last_name", "distance"):
        key = item["marathon"]
        grouped[key].append({k: v for k, v in item.items() if k != "marathon"})
    
    # JSON 변환
    json_result = json.dumps(grouped, ensure_ascii=False, indent=2)
    marathon = json.loads(json_result)
    
    return render(request, 'marathon.html', {'group':marathon})

def parti_me(request, key):
    if request.method == "POST":
        marathon_title = MarathonEvent.objects.get(marathon_id=key)
        marathonreg = MarathonReg()
        marathonreg.marathon = marathon_title
        marathonreg.user = request.user
        marathonreg.distance = request.POST["distance"]
        marathonreg.save()
        return redirect("marathon:marathon_list")
    else:
        return render(request, "marathon.html")