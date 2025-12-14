from datetime import timedelta
from django.shortcuts import redirect, render
from django.db.models import Sum
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from record.models import *

# Create your views here.

def runres(request):
    return render(request,"run_res.html")

def recordres(request):
    pk = request.user.id
    if request.method == "POST":
        record = Record()
        record.title = request.POST["title"]
        record.user = request.user
        record.record_date = request.POST["record_date"]
        record.image = request.FILES["image"]
        record.distance = request.POST["distance"]
        record.pace_m = request.POST["pace_m"]
        record.pace_s = request.POST["pace_s"]
        if request.POST["time_h"] == '':
            record.time_h = None
        else:
            record.time_h = request.POST["time_h"]
        record.time_m = request.POST["time_m"]
        record.time_s = request.POST["time_s"]
        record.desc = request.POST["desc"]
        record.save()
        return redirect("runres:recordview",pk=pk)
    else:
        return redirect("runres:recordview",pk=pk)

def recordview(request,pk):

    month = request.GET.get('month')

    if month =="0" or month == None:
        month = "0"
        record_list = Record.objects.filter(user=pk).order_by('-record_date')
        distance_sum = Record.objects.filter(confirmed=True).filter(user=pk).aggregate(Sum('distance'))
        distance_sum_not = Record.objects.filter(user=pk).aggregate(Sum('distance'))
        
    else:
        record_list = Record.objects.filter(user=pk).filter(record_date__month=month).order_by('-record_date')
        distance_sum = Record.objects.filter(confirmed=True).filter(user=pk).filter(record_date__month=month).aggregate(Sum('distance'))
        distance_sum_not = Record.objects.filter(user=pk).filter(record_date__month=month).aggregate(Sum('distance'))
    
    page = int(request.GET.get('p', 1)) #없으면 1로 지정
    paginator = Paginator(record_list, 3) #한 페이지 당 몇개 씩 보여줄 지 지정
    record_list = paginator.get_page(page)

    return render(request,"run_record.html", {"context":record_list, "distance_sum":distance_sum, "month": month, "distance_sum_not":distance_sum_not})

def recordUpdateView(request,pk,record_id):
    record = Record.objects.filter(user=pk).get(record_id=record_id)
    return render(request,"run_update.html", {"record_id":record_id, "record":record})

def recordUpdate(request,pk,record_id):
    record = Record.objects.filter(user=pk).get(record_id=record_id)
    if request.method == "POST":
        record.title = request.POST["title"]
        record.user = request.user
        record.record_date = request.POST["record_date"]
        if request.FILES.get("image") is not None:
            record.image = request.FILES["image"]
        record.distance = request.POST["distance"]
        record.pace_m = request.POST["pace_m"]
        record.pace_s = request.POST["pace_s"]
        if request.POST["time_h"] == '':
            record.time_h = None
        else:
            record.time_h = request.POST["time_h"]
        record.time_m = request.POST["time_m"]
        record.time_s = request.POST["time_s"]
        record.desc = request.POST["desc"]
        record.save()
        return redirect("runres:recordview",pk=pk)
    else:
        return redirect("runres:recordview",pk=pk)
    

def recordRank(request):
    month = request.GET.get('month')
    team = request.GET.get('team')
    team_list = Team.objects.all()

    if (month =="0" or month == None) and team == None:
        record = Record.objects.values('user__username','user__first_name','user__last_name').annotate(record_sum=Sum('distance')).order_by('-record_sum')
        distance_sum = Record.objects.filter(confirmed=True).aggregate(Sum('distance'))
    elif (month =="0" or month == None) and team != None:
        record = Record.objects.values('user__username','user__first_name','user__last_name').annotate(record_sum=Sum('distance')).order_by('-record_sum').filter(user__teammember__team=team)
        distance_sum = record.filter(confirmed=True).aggregate(Sum('distance'))
        team = Team.objects.get(team_id = team)
    else:
        record = Record.objects.filter(record_date__month=month).values('user__username','user__first_name','user__last_name').annotate(record_sum=Sum('distance')).order_by('-record_sum')
        distance_sum = Record.objects.filter(confirmed=True).filter(record_date__month=month).aggregate(Sum('distance'))
    return render(request, "record_rank.html", {"record_rank":record, "month":month, "distance_sum":distance_sum, "team":team, "team_list":team_list})

def recordCheck(request):
    record = Record.objects.order_by('-record_date')
    return render(request,"record_check.html", {"record":record})

def recordConfirm(request,id):
    if request.method == "POST":
        record = Record.objects.get(record_id=id)
        record.confirmed = True
        record.save()
    return redirect("runres:recordCheck")

def recordReject(request,id):
    if request.method == "POST":
        record = Record.objects.get(record_id=id)
        record.confirmed = False
        record.save()
    return redirect("runres:recordCheck")

def recordDelete(request,id):
    if request.method == "POST":
        record = Record.objects.get(record_id=id)
        record.confirmed = False
        record.delete()
    return redirect("runres:recordCheck")

def pbRank(request):
    try:
        ranking_tenk = PersonalRecord.objects.filter(category='10K').order_by('record')
        ranking_hm = PersonalRecord.objects.filter(category='HM').order_by('record')
        ranking_fm = PersonalRecord.objects.filter(category='FM').order_by('record')
        print(ranking_fm)
    except:
        ranking_tenk = None 
        ranking_hm = None
        ranking_fm = None   
    return render(request,"run_pb.html", {"ranking_tenk":ranking_tenk, "ranking_hm":ranking_hm, "ranking_fm":ranking_fm})

@login_required
def pbView(request,pk):
    pb_tenk = PersonalRecord.objects.filter(runner=pk).filter(category='10K').first()
    pb_hm = PersonalRecord.objects.filter(runner=pk).filter(category='HM').first()
    pb_fm = PersonalRecord.objects.filter(runner=pk).filter(category='FM').first()

    return render(request,"run_mypb.html", {"pb_tenk":pb_tenk, "pb_hm":pb_hm, "pb_fm":pb_fm})

@login_required
def pbresPage(request,pk,category):
    return render(request,"run_pb_res.html",{"category":category})

@login_required
def pbRes(request, pk, category):
    if request.method == "POST":
        mypb = PersonalRecord()
        if request.POST["time_h"] == "":
            h = 0
        else:
            h = int(request.POST["time_h"])
        m = int(request.POST["time_m"])
        s = int(request.POST["time_s"])
        mypb.event_name = request.POST["title"]
        mypb.runner = request.user
        mypb.date = request.POST["date"]
        mypb.evidence_url = request.FILES["image"]
        mypb.category = category
        mypb.record = timedelta(hours=h, minutes=m, seconds=s)
        mypb.desc = request.POST["desc"]
        mypb.save()
        return redirect("runres:pbView", pk)
    else:
        return redirect("runres:pbView", pk)

@login_required
def pbUpdateView(request,pk,category):
    record = PersonalRecord.objects.filter(runner=pk).filter(category=category).first()
    return render(request,"run_pb_update.html", {"record":record})

@login_required
def pbUpdate(request,pk,category):

    record = PersonalRecord.objects.filter(runner=pk).get(category=category)

    if request.method == "POST":
        if request.POST["time_h"] == "":
            h = 0
        else:
            h = int(request.POST["time_h"])
        m = int(request.POST["time_m"])
        s = int(request.POST["time_s"])
        record.event_name = request.POST["title"]
        record.runner = request.user
        record.date = request.POST["date"]
        record.status = "pending"
        record.evidence_url = request.FILES["image"]
        record.category = category
        record.record = timedelta(hours=h, minutes=m, seconds=s)
        record.desc = request.POST["desc"]
        record.save()
        return redirect("runres:pbView", pk)
    else:
        return redirect("runres:pbView", pk)

def runPbCheck(request):
    record = PersonalRecord.objects.order_by('-created_at')
    return render(request,"run_pb_check.html", {"record":record})

def pbConfirm(request,id):
    if request.method == "POST":
        record = PersonalRecord.objects.get(id=id)
        record.status = 'verified'
        record.save()
    return redirect("runres:runPbCheck")

def pbReject(request,id):
    if request.method == "POST":
        record = PersonalRecord.objects.get(id=id)
        record.status = 'rejected'
        record.save()
    return redirect("runres:runPbCheck")

def pbDelete(request,id):
    if request.method == "POST":
        record = PersonalRecord.objects.get(id=id)
        record.delete()
    return redirect("runres:runPbCheck")

def team_assign_view(request):
    teams = Team.objects.all()
    users = User.objects.all()

    # 현재 팀 배정 정보 맵핑
    tm = TeamMember.objects.select_related('user', 'team')
    current_map = {t.user_id: t.team_id for t in tm}

    # users 에 current_team_id 속성을 임시로 붙이기
    for u in users:
        u.current_team_id = current_map.get(u.id)

    return render(request, "team_assign.html", {
        "teams": teams,
        "members": users,  # 템플릿에서 members 로 사용
    })

@require_POST
def save_team_members(request):
    for key, value in request.POST.items():
        print(key)
        print(value)
        if not key.startswith("member_team_"):
            continue

        user_id = key.replace("member_team_", "")
        team_id = value or None

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            continue

        # 기존 팀 정보 제거
        TeamMember.objects.filter(user=user).delete()

        if team_id:
            team = Team.objects.get(team_id=team_id)
            TeamMember.objects.create(
                user=user,
                team=team,
                leader=False,
            )

    return redirect("runres:team_assign_view")  # 팀 편집 페이지로 되돌아가기