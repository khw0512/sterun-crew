from collections import defaultdict
import json
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse 
from django.core import serializers
from django.db.models import Q
from django.db.models import Max
from datetime import datetime

from marathon.models import *

def marathon_list(request):
    marathon = MarathonReg.objects.select_related("marathon").order_by("marathon_id")

    grouped = defaultdict(list)
    for item in marathon.values("id", "marathon__title", "user__username", "user__first_name", "user__last_name"):
        key = item["marathon__title"]
        grouped[key].append({k: v for k, v in item.items() if k != "marathon__title"})
    
    # JSON 변환
    json_result = json.dumps(grouped, ensure_ascii=False, indent=2)
    marathon = json.loads(json_result)
    print(marathon)
    
    return render(request, 'marathon.html', {'group':marathon})