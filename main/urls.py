from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('go-back/', views.go_back_view, name='go_back'),
]