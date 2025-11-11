from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse 
from django.core import serializers
from django.db.models import Q
from django.db.models import Max
from datetime import datetime

from marathon.models import *

def marathon_list(request):
    marathon = MarathonReg.objects.select_related("marathon").order_by("marathon_id")
    print(marathon)
    context = {'marathon': marathon}
    return render(request, 'marathon.html', context)