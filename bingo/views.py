from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Sum
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from bingo.models import *
from record.models import Record

def bingo(request, pk):
    user = get_object_or_404(User, pk=pk)
    login_user = request.user
    if user == login_user:
        user_matched = 1
    else:
        user_matched = None
    print(user_matched)
    bingo_item_1r = BingoCheck.objects.select_related("bingo_item").filter(user=pk).filter(bingo_item__row=1)
    bingo_item_2r = BingoCheck.objects.select_related("bingo_item").filter(user=pk).filter(bingo_item__row=2)
    bingo_item_3r = BingoCheck.objects.select_related("bingo_item").filter(user=pk).filter(bingo_item__row=3)
    bingo_item_4r = BingoCheck.objects.select_related("bingo_item").filter(user=pk).filter(bingo_item__row=4)
    bingo_item_5r = BingoCheck.objects.select_related("bingo_item").filter(user=pk).filter(bingo_item__row=5)
    lenof5l = len(bingo_item_5r)
    return render(request,"bingo.html",{"bingo_item_1r":bingo_item_1r, "bingo_item_2r":bingo_item_2r, "bingo_item_3r":bingo_item_3r, "bingo_item_4r":bingo_item_4r, "bingo_item_5r":bingo_item_5r, "user_id":pk, "len":lenof5l,"user_name":user.username, "user_matched":user_matched})

def create_bingo(request, pk):
    i = 1
    while i <= 25:
        bingoitem = BingoItem.objects.filter(item_id = i)
        existing = BingoCheck.objects.filter(bingo_item = bingoitem[0]).filter(user=request.user).exists()
        print(bingoitem)
        if not existing:
            bingocheck = BingoCheck(
                bingo_item = bingoitem[0],
                user = request.user,
                completed = False
            )
            bingocheck.save()
            print(request.user)
        i+=1
    return redirect("bingo:bingo", pk)


def update_public_status(request,pk):
    log_user = request.user
    bin_user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        bingo_id = data.get("bingo_id")
        is_checked = data.get("is_checked")
        print(is_checked)
        if log_user == bin_user:
            try:
                bingo_item = BingoCheck.objects.filter(user=request.user).get(bingo_item__item_id=bingo_id)
                if is_checked == False:
                    bingo_item.completed = False
                    bingo_item.save()
                else:
                    bingo_item.completed = True
                    bingo_item.save()
                return JsonResponse({"status": "success", "checked": bingo_item.completed})
            except BingoCheck.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Post not found"}, status=404)
        else:
            return JsonResponse({"status": "success", "message": "log_user is not bin_user"})

    return JsonResponse({"error": "Invalid request"}, status=400)

def bingoupdate(request,pk):

    bingoitem = BingoItem.objects.all()
    
    return render(request, "bingo_res.html", {"bingoitem":bingoitem})

def bingores(request, pk):

    if request.method == "POST":
        items = BingoItem.objects.all()

        i=1
        while i < 26:
            BingoItem.objects.filter(item_id=i).update(content=request.POST.get("content"+str(i)))
            i+=1
        return render(request, "index.html")
    else:
        return render(request, "index.html")