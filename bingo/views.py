from django.shortcuts import redirect, render
from django.db.models import Sum
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from bingo.models import *
from record.models import Record

def bingo(request, pk):
    bingo_item_1r = BingoCheck.objects.select_related("bingo_item").filter(bingo_item__row=1)
    bingo_item_2r = BingoCheck.objects.select_related("bingo_item").filter(bingo_item__row=2)
    bingo_item_3r = BingoCheck.objects.select_related("bingo_item").filter(bingo_item__row=3)
    bingo_item_4r = BingoCheck.objects.select_related("bingo_item").filter(bingo_item__row=4)
    bingo_item_5r = BingoCheck.objects.select_related("bingo_item").filter(bingo_item__row=5)
    print(bingo_item_1r)
    return render(request,"bingo.html",{"bingo_item_1r":bingo_item_1r, "bingo_item_2r":bingo_item_2r, "bingo_item_3r":bingo_item_3r, "bingo_item_4r":bingo_item_4r, "bingo_item_5r":bingo_item_5r})

def create_bingo(request, pk):
    i = 1
    while i <= 25:
        bingoitem = BingoItem.objects.filter(item_id = i    )
        existing = BingoCheck.objects.filter(bingo_item = bingoitem[0]).exists()
        print(bingoitem)
        if not existing:
            bingocheck = BingoCheck(
                bingo_item = bingoitem[0],
                user = request.user,
                completed = False
            )
            bingocheck.save()
        i+=1
    return redirect("bingo:bingo", pk)


def update_public_status(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        bingo_id = data.get("bingo_id")
        is_checked = data.get("is_checked")
        print(is_checked)

        try:
            bingo_item = BingoCheck.objects.get(bingo_item__item_id=bingo_id)
            if is_checked == False:
                bingo_item.completed = False
                bingo_item.save()
            else:
                bingo_item.completed = True
                bingo_item.save()
            return JsonResponse({"status": "success", "checked": bingo_item.completed})
        except BingoCheck.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Post not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)