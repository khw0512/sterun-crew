from django.shortcuts import render
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from django.utils.dateformat import DateFormat
import math

from bingo.models import *
from record.models import Record


def index(request):
    return render(request,"index.html")

def go_back_view(request):
    # 이전 페이지 URL을 가져오되, 없을 경우 홈('/')으로 리디렉트
    previous_url = request.META.get('HTTP_REFERER', '/')
    print(previous_url)
    return redirect(previous_url)

def setting_page(request):
    bingoitem = BingoItem.objects.all() 
    cnt_items = bingoitem.count()
    return render(request,"admin/setting.html",{"cnt_items":cnt_items} )