from django.shortcuts import render
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from django.utils.dateformat import DateFormat
import math


def attendance(request):
    return render(request,"index.html")
