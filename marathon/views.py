from collections import defaultdict
import json
from django.shortcuts import render, redirect
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
    print(events)
    context = {
        'events': events,
    }
    
    return render(request, 'marathon.html', context)


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
    
'''
def del_parti(request, id):
    if request.method == "POST":
        marathon = MarathonReg.objects.get(record_id=id)
'''