from django.urls import path

from . import views

app_name = "runres"

urlpatterns = [
    path("resister/", views.runres, name="runres"),
    path('recordres/', views.recordres, name='recordres'),
    path('recordview/<str:pk>/', views.recordview, name='recordview'),
]