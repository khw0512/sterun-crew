from django.urls import path

from . import views

app_name = "bingo"

urlpatterns = [
    path("<str:pk>", views.bingo, name="bingo"),
    path("createbingo/<str:pk>", views.create_bingo, name="create_bingo"),
    path("update-public-status/<str:pk>", views.update_public_status, name="update_public_status"),
    path("bingoupdate/<str:pk>", views.bingoupdate, name="bingoupdate"),
    path("bingores/<str:pk>", views.bingores, name="bingores"),
    path("bingoreset/", views.bingoreset, name="bingoreset"),
]