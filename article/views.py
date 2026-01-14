from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse 
from django.core import serializers
from django.db.models import Q
from django.db.models import Max
from datetime import datetime

from article.models import *

# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    recentatc = Article.objects.last()
    recent_id_dic = Article.objects.aggregate(id=Max('id'))
    recent_id = recent_id_dic['id']
    oldatc = Article.objects.all().order_by('-pub_date').exclude(id=recent_id)
    # page = int(request.GET.get('page', 1))  # 없으면 1로 지정
    # paginator = Paginator(oldatc, 3)  # 한 페이지 당 몇개 씩 보여줄 지 지정
    #boards = paginator.get_page(page)
    context = {'articles': articles, 'recentatc': recentatc,
               'oldatc': oldatc}
    return render(request, 'article/collabo_main.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'article/collabo_article.html', context)


def search(request):
    articles = Article.objects.all().order_by('-pub_date')
    recentatc = Article.objects.last()
    recent_id_dic = Article.objects.aggregate(id=Max('id'))
    recent_id = recent_id_dic['id']
    oldatc = Article.objects.all().order_by('-pub_date').exclude(id=recent_id)
    if request.method == 'POST':
        searched = request.POST['searched']
        results = oldatc.filter(
            Q(title__contains=searched) | Q(desc__contains=searched))
        # page = int(request.GET.get('page', 1))  # 없으면 1로 지정
        # paginator = Paginator(results, 3)  # 한 페이지 당 몇개 씩 보여줄 지 지정
        #boards = paginator.get_page(page)
        context = {'articles': articles,
                   'recentatc': recentatc, 'oldatc': oldatc, 'searched': searched, 'results': results}
        print(searched)
        return render(request, 'article/searched.html', context)
    else:
        return render(request, 'article/searched.html', {'articles': articles, 'recentatc': recentatc, 'oldatc': oldatc, 'searched': False})


def alldata(request):
    articles = Article.objects.all().order_by('-pub_date')
    recentatc = Article.objects.last()
    recent_id_dic = Article.objects.aggregate(id=Max('id'))
    recent_id = recent_id_dic['id']
    oldatc = Article.objects.all().order_by('-pub_date').exclude(id=recent_id)
    # page = int(request.GET.get('page', 1))  # 없으면 1로 지정
    # paginator = Paginator(oldatc, 3)  # 한 페이지 당 몇개 씩 보여줄 지 지정
    # boards = paginator.get_page(page)
    all_data = serializers.serialize("json", oldatc)
    context = {'articles': articles, 'recentatc': recentatc,
               'oldatc': oldatc}
    print(context)
    return JsonResponse(all_data, safe=False)


def searchTitle(request):
    keyword = request.GET.get('keyword')
    articles = Article.objects.all().order_by('-pub_date')
    recentatc = Article.objects.last()
    recent_id_dic = Article.objects.aggregate(id=Max('id'))
    recent_id = recent_id_dic['id']
    oldatc = Article.objects.all().order_by('-pub_date').exclude(id=recent_id)
    results = oldatc.filter(
        Q(title__contains=keyword) | Q(desc__contains=keyword))
    context = {'articles': articles,
               'recentatc': recentatc, 'oldatc': oldatc, 'keyword': keyword, 'results': results}
    all_data = serializers.serialize("json", results)
    print(all_data)
    return JsonResponse(all_data, safe=False)

    #dict = {'test': keyword}
    # return HttpResponse(json.dumps(dict), content_type='application/json')

def articleRes(request):
    return render(request, "admin/collabo_article_res.html")

def articleResFunc(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST["title"]
        article.brand = request.POST["brand"]
        article.model = request.POST["model"]
        article.author = request.user
        article.content = request.POST["content"]
        article.main_img = request.FILES["image"]
        article.pub_date = datetime.now()
        article.save()
        return render(request, "index.html")
    else:
        return render(request, "index.html")