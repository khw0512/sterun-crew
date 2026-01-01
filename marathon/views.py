from collections import defaultdict
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, JsonResponse 
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.db.models import Max
from datetime import datetime

from marathon.models import *


def marathon_list(request):
    events = MarathonEvent.objects.prefetch_related(
        'marathonreg_set__user'   # 역참조 + user까지 미리 가져오기
    )
    context = {
        'events': events,
    }
    
    return render(request, 'marathon/marathon.html', context)


def parti_me(request, key):
    if request.method == "POST":
        if MarathonReg.objects.filter(user=request.user).filter(marathon=key).exists():
            print(key)
            return redirect("marathon:marathon_list")
        else:
            MarathonEvent.objects.get(marathon_id=key)
            marathon_title = MarathonEvent.objects.get(marathon_id=key)
            marathonreg = MarathonReg()
            marathonreg.marathon = marathon_title
            marathonreg.user = request.user
            marathonreg.distance = request.POST["distance"]
            marathonreg.save()
            return redirect("marathon:marathon_list")
    else:
        return redirect("marathon:marathon_list")
    

def del_parti(request, key):
    if request.method == "POST":
        marathon = get_object_or_404(MarathonReg,regis_id=key)
        marathon.delete()
    return redirect("marathon:marathon_list")
