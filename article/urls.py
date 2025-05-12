from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'article'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_id>/", views.article, name="article"),
    path("search/", views.search, name="search"),
    path("alldata/", views.alldata, name="alldata"),
    path("searchtitle/", views.searchTitle, name='searchtitle'),
    path("articleres/", views.articleRes, name='articleres'),
    path("articleresfunc/", views.articleResFunc, name='articleresfunc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)