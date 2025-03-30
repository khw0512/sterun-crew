from django.shortcuts import redirect, render
from django.db.models import Sum
from django.core.paginator import Paginator

from record.models import Record

def bingo(request):
    return render(request,"bingo.html")