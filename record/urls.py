from django.urls import path

from . import views

app_name = "runres"

urlpatterns = [
    path("resister/", views.runres, name="runres"),
    path('recordres/', views.recordres, name='recordres'),
    path('recordview/<str:pk>/', views.recordview, name='recordview'),
    path('recordUpdateView/<str:pk>/<str:record_id>', views.recordUpdateView, name='recordUpdateView'),
    path('recordUpdate/<str:pk>/<str:record_id>', views.recordUpdate, name='recordUpdate'),
    path('recordrank/', views.recordRank, name="recordRank"),
    path('recordCheck/', views.recordCheck, name="recordCheck"),
    path('recordConfirm/<str:id>', views.recordConfirm, name="recordConfirm"),
    path('recordReject/<str:id>', views.recordReject, name="recordReject"),
    path('recordDelete/<str:id>', views.recordDelete, name="recordDelete"),
    path('pbrank/', views.pbRank, name="pbRank"),
    path('pbview/<str:pk>/', views.pbView, name="pbView"),
    path('pbresPage/<str:pk>/<str:category>/', views.pbresPage, name="pbresPage"),
    path('pbRes/<str:pk>/<str:category>/', views.pbRes, name="pbRes"),
    path('pbUpdateView/<str:pk>/<str:category>/', views.pbUpdateView, name="pbUpdateView"),
    path('pbUpdate/<str:pk>/<str:category>/', views.pbUpdate, name="pbUpdate"),
]